import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
class VoteClassifier(ClassifierI):
    def __init__(self, *classsifiers):
        self._classifiers = classsifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf


# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
#
# #random.shuffle(documents)
#
# all_words = []
#
# for w in movie_reviews.words():
#     all_words.append(w.lower())

short_pos = open("short_reviews/positive.txt", "r").read()
short_neg = open("short_reviews/negative.txt", "r").read()

documents = []
for r in short_pos.split("\n"):
    documents.append((r,"pos"))

for r in short_neg.split("\n"):
    documents.append((r,"neg"))

all_words = []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())

for w in short_neg_words:
    all_words.append(w.lower())


all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
#print((find_features(movie_reviews.words('neg/file.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
# set that we'll train our classifier with
training_set = featuresets[:10000]
# set that we'll test against.
testing_set = featuresets[10000:]



classifier = nltk.NaiveBayesClassifier.train(training_set)

# classifier_f = open("naiveBayes.pickle","rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()
#testing_set[5][0]

##save_classifier = open("naiveBayes.pickle","wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()

print("Original Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier,
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)

print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

# print("Classification: ", voted_classifier.classify(testing_set[0][0]), "Confidence %:", voted_classifier.confidence(testing_set[0][0])*100)
# print("Classification: ", voted_classifier.classify(testing_set[1][0]), "Confidence %:", voted_classifier.confidence(testing_set[1][0])*100)
# print("Classification: ", voted_classifier.classify(testing_set[2][0]), "Confidence %:", voted_classifier.confidence(testing_set[2][0])*100)
# print("Classification: ", voted_classifier.classify(testing_set[3][0]), "Confidence %:", voted_classifier.confidence(testing_set[3][0])*100)
# print("Classification: ", voted_classifier.classify(testing_set[4][0]), "Confidence %:", voted_classifier.confidence(testing_set[4][0])*100)
# print("Classification: ", voted_classifier.classify(testing_set[5][0]), "Confidence %:", voted_classifier.confidence(testing_set[5][0])*100)

