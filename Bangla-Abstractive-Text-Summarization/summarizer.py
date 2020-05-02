from attention import AttentionLayer
import numpy as np  
import pandas as pd 
import re           
from bs4 import BeautifulSoup 
from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Bidirectional, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import warnings
from sklearn.model_selection import train_test_split
from keras import backend as K
import tensorflow as tf
import os
from tensorflow import keras
from sklearn.model_selection import train_test_split


pd.set_option("display.max_colwidth", 200)
warnings.filterwarnings("ignore")

trainData = pd.read_excel("knn and naive bayes.xlsx")

print("Data files read")

def text_cleaner(text):
    tokens = [w for w in text.split()]
    return (" ".join(tokens)).strip()

cleaned_text = []
for t in trainData['Text']:
    cleaned_text.append(text_cleaner(str(t)))
    
cleaned_summary = []
for t in trainData['Summary']:
    cleaned_summary.append(text_cleaner(str(t)))


trainData['cleaned_text']=cleaned_text
trainData['cleaned_summary']=cleaned_summary

print("Data files cleaned")

trainData['cleaned_text']=cleaned_text
trainData['cleaned_summary']=cleaned_summary


trainData['cleaned_summary'] = trainData['cleaned_summary'].apply(lambda x : 'sostok '+ x + ' eostok')

max_len_text=100 
max_len_summary=10



x_tr,x_test_gt,y_tr,y_test_gt=train_test_split(np.array(trainData['cleaned_text']),np.array(trainData['cleaned_summary']),test_size=0.01,random_state=0,shuffle=True)
x_tr,x_val,y_tr,y_val=train_test_split(np.array(x_tr),np.array(y_tr),test_size=0.1,random_state=0,shuffle=True)

testArticles_gt = list(x_test_gt)
testSummaries_gt = list(y_test_gt)
#x_tr = trainData['cleaned_text']
#y_tr = trainData['cleaned_summary']

#x_val = testData['cleaned_text']
#y_val = testData['cleaned_summary']

print(len(x_tr), len(y_tr), len(x_val), len(y_val))
print(len(x_test_gt), len(y_test_gt))

x_tokenizer = Tokenizer()
x_tokenizer.fit_on_texts(list(x_tr))

x_tr = x_tokenizer.texts_to_sequences(x_tr) 
x_val = x_tokenizer.texts_to_sequences(x_val)
x_test_gt = x_tokenizer.texts_to_sequences(x_test_gt)

x_tr = pad_sequences(x_tr,  maxlen=max_len_text, padding='post') 
x_val = pad_sequences(x_val, maxlen=max_len_text, padding='post')
x_test_gt = pad_sequences(x_test_gt, maxlen=max_len_text, padding='post')

x_voc_size = len(x_tokenizer.word_index)+1


y_tokenizer = Tokenizer()
y_tokenizer.fit_on_texts(list(y_tr))

y_tr = y_tokenizer.texts_to_sequences(y_tr) 
y_val = y_tokenizer.texts_to_sequences(y_val)
y_test_gt = y_tokenizer.texts_to_sequences(y_test_gt)

y_tr = pad_sequences(y_tr, maxlen=max_len_summary, padding='post')
y_val = pad_sequences(y_val, maxlen=max_len_summary, padding='post')
y_test_gt = pad_sequences(y_test_gt, maxlen=max_len_summary, padding='post')

y_voc_size = len(y_tokenizer.word_index)+1


K.clear_session() 
latent_dim = 1024
embedding_dim = 1024

encoder_inputs = Input(shape=(max_len_text,)) 
enc_emb = Embedding(x_voc_size, embedding_dim,trainable=True)(encoder_inputs) 




#LSTM 1
encoder_lstm1 = (LSTM(latent_dim,return_sequences=True,return_state=True))
encoder_output1, state_h1, state_c1 = encoder_lstm1(enc_emb) 

#LSTM 2 
#encoder_lstm2 = (LSTM(latent_dim,return_sequences=True,return_state=True))
#encoder_output2, state_h2, state_c2 = encoder_lstm2(encoder_output1)

#LSTM 3
encoder_lstm3 = (LSTM(latent_dim, return_state=True, return_sequences=True))
encoder_outputs, state_h, state_c= encoder_lstm3(encoder_output1)
#encoder_outputs, state_h, state_c= encoder_lstm3(enc_emb)

# Set up the decoder. 
decoder_inputs = Input(shape=(None,)) 
dec_emb_layer = Embedding(y_voc_size, embedding_dim,trainable=True) 
dec_emb = dec_emb_layer(decoder_inputs) 

#LSTM using encoder_states as initial state
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True) 
decoder_outputs,decoder_fwd_state, decoder_back_state = decoder_lstm(dec_emb,initial_state=[state_h, state_c]) 

#Attention Layer
attn_layer = AttentionLayer(name='attention_layer') 
attn_out, attn_states = attn_layer([encoder_outputs, decoder_outputs]) 

# Concat attention output and decoder LSTM output 
decoder_concat_input = Concatenate(axis=-1, name='concat_layer')([decoder_outputs, attn_out])

#Dense layer
decoder_dense = TimeDistributed(Dense(y_voc_size, activation='softmax')) 
decoder_outputs = decoder_dense(decoder_concat_input) 

# Define the model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs) 
print("Model constructed\n\n")
model.summary()
print("\n\n")

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')

checkpoint_path = "model-1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=3, restore_best_weights=True)
cp_callback = ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)
initial_epoch = 0

if os.path.exists(checkpoint_path+".index")==False:
    print("No model saved.")
else:
    print("Model loaded.")
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    initial_epoch = 0
    model.load_weights(latest)


history=model.fit([x_tr,y_tr[:,:-1]], 
                y_tr.reshape(y_tr.shape[0],y_tr.shape[1], 1)[:,1:],
                epochs=25,
                initial_epoch=initial_epoch,
                callbacks=[es, cp_callback],
                batch_size=128,
                validation_data=([x_val,y_val[:,:-1]],
                y_val.reshape(y_val.shape[0],y_val.shape[1], 1)[:,1:]))


reverse_target_word_index=y_tokenizer.index_word 
reverse_source_word_index=x_tokenizer.index_word 
target_word_index=y_tokenizer.word_index


# encoder inference
encoder_model = Model(inputs=encoder_inputs,outputs=[encoder_outputs, state_h, state_c])

# decoder inference
# Below tensors will hold the states of the previous time step
decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_hidden_state_input = Input(shape=(max_len_text,latent_dim))

# Get the embeddings of the decoder sequence
dec_emb2= dec_emb_layer(decoder_inputs)

# To predict the next word in the sequence, set the initial states to the states from the previous time step
decoder_outputs2, state_h2, state_c2 = decoder_lstm(dec_emb2, initial_state=[decoder_state_input_h, decoder_state_input_c])

#attention inference
attn_out_inf, attn_states_inf = attn_layer([decoder_hidden_state_input, decoder_outputs2])
decoder_inf_concat = Concatenate(axis=-1, name='concat')([decoder_outputs2, attn_out_inf])

# A dense softmax layer to generate prob dist. over the target vocabulary
decoder_outputs2 = decoder_dense(decoder_inf_concat)

# Final decoder model
decoder_model = Model(
[decoder_inputs] + [decoder_hidden_state_input,decoder_state_input_h, decoder_state_input_c],
[decoder_outputs2] + [state_h2, state_c2])


def decode_sequence(input_seq):
    #print(tf.shape(input_seq))
    # Encode the input as state vectors.
    e_out, e_h, e_c = encoder_model.predict(input_seq)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1,1))

    # Chose the 'start' word as the first word of the target sequence
    target_seq[0, 0] = target_word_index['sostok']

    stop_condition = False
    decoded_sentence = ''
    i = 0
    while not stop_condition:
        i+=1
        output_tokens, h, c = decoder_model.predict([target_seq] + [e_out, e_h, e_c])

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        if sampled_token_index in reverse_target_word_index:
            sampled_token = reverse_target_word_index[sampled_token_index]
        else:
            sampled_token = "<PAD>"
        if i%50==0:
            print(decoded_sentence)
        if(sampled_token!='eostok'):
            decoded_sentence += ' '+sampled_token

            # Exit condition: either hit max length or find stop word.
            if (sampled_token == 'eostok' or len(decoded_sentence.split()) >= (max_len_summary-1)) or sampled_token=="\n":
                stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1,1))
        target_seq[0, 0] = sampled_token_index

        # Update internal states
        e_h, e_c = h, c

    return decoded_sentence


def seq2summary(input_seq):
    newString=''
    for i in input_seq:
        if((i!=0 and i!=target_word_index['sostok']) and i!=target_word_index['eostok']):
            newString=newString+reverse_target_word_index[i]+' '
    return newString

def seq2text(input_seq):
    newString=''
    for i in input_seq:
        if(i!=0):
            if i not in reverse_source_word_index:
                newString+="unk"
            else:
                newString=newString+reverse_source_word_index[i]+' '
    return newString


print("Model generated.\n\n")


folder_num = "1"


outputFile = open("output-"+folder_num+"/generated_summaries.txt", "w+")
comparisonFile = open("output-"+folder_num+"/output_comparison.txt", "w+")
refSum = open("output-"+folder_num+"/reference_sums.txt", "w+")

print("Testing on automated translated knn and naive bayes...\n\n\n")


for i in range(len(x_test_gt)):
    if i%100==0 or i==len(x_test_gt)-1:
        print(str(i)+"/"+str(len(x_test_gt)))
    art = testArticles_gt[i]
    #print("Review:",art)
    comparisonFile.write("Article:-\n")
    comparisonFile.write(art)
    comparisonFile.write("\n\nReference summary:-\n")
    ogS = testSummaries_gt[i]
    #print("Original summary:",ogS)
    comparisonFile.write(ogS)
    refSum.write(ogS+"\n")
    try:
        sm = decode_sequence(x_test_gt[i].reshape(1,max_len_text))
        #print("Predicted summary:",sm)
        comparisonFile.write("\n\nPredicted summary:-\n")
        comparisonFile.write(sm)
        comparisonFile.write("\n\n")
        outputFile.write(sm)
        outputFile.write("\n")
    except ValueError:
        print("Error")
        continue
    #print("\n")
    
outputFile.close()
comparisonFile.close()
refSum.close()

print("Done")













