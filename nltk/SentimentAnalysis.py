import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifier = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifier:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifier:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


reviews = [(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

# shuffle all reviews
random.shuffle(reviews)

# Get all the words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Get frequency for each of these words
all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(10))
# print(all_words['good'])
# print(type(all_words))

word_features = list(all_words.keys())[:3000]


def find_features(review):
    words = set(review)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


featuresets = [(find_features(rev), category) for (rev, category) in reviews]

train = featuresets[:1900]
test = featuresets[1900:]
print(test[0][1])
# classifier = nltk.NaiveBayesClassifier.train(train)
classifier_f = open('naiveBayesMovieReview.pickle', 'rb')
classifier = pickle.load(classifier_f)
classifier_f.close()
print("Test accuracy precentage is : ", (nltk.classify.accuracy(classifier, test)) * 100)
classifier.show_most_informative_features(15)

# save_classifier = open('naiveBayesMovieReview.pickle', 'wb')
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train)
print("MNB classifier accuracy percentage: ", nltk.classify.accuracy(MNB_classifier, test) * 100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(train)
print("BernoulliNB_classifier accuracy percentagse: ",
      (nltk.classify.accuracy(BernoulliNB_classifier, test)) * 100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(train)
print("Logistic Regression accuracy percentage: ",
      (nltk.classify.accuracy(LogisticRegression_classifier, test)) * 100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(train)
print("SGDC Classifier accuracy percentage: ",
      (nltk.classify.accuracy(SGDClassifier_classifier, test)) * 100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(train)
print("SVC Classifier accuracy percentage: ", (nltk.classify.accuracy(SVC_classifier, test)) * 100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(train)
print("Linear SVC accuracy percentage: ", (nltk.classify.accuracy(LinearSVC_classifier, test)) * 100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(train)
print("NuSVC classifier accuracy percentage: ",
      (nltk.classify.accuracy(NuSVC_classifier, test)) * 100)

voted_classifier = VoteClassifier(classifier,
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)

print('Voteed_classifier accuracy percentage: ',
      nltk.classify.accuracy(voted_classifier, test) * 100)
