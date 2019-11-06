import tensorflow as tf
num_nodes = 128
batch_size = 64
num_unrollings = 50
dropout = 0.2
vocabulary_size =128
ix = tf.Variable(tf.truncated_normal([vocabulary_size, num_nodes],stddev=0.02))