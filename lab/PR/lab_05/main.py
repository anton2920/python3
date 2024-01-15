from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_files
import numpy as np

# Training data.
reviews_train = load_files(r"C:\Users\Anton\PycharmProjects\4\lab_03\aclImdb\train")
text_train, y_train = reviews_train.data, reviews_train.target
text_train = [doc.replace(b"<br />", b" ") for doc in text_train]

print("Number of examples per class (training): {}".format(np.bincount(y_train)))

# Testing data.
reviews_test = load_files(r"C:\Users\Anton\PycharmProjects\4\lab_03\aclImdb\test")
text_test, y_test = reviews_test.data, reviews_test.target
text_test = [doc.replace(b"<br />", b" ") for doc in text_test]

vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=5, stop_words="english")
X_train = vectorizer.fit_transform(text_train)
X_test = vectorizer.transform(text_test)

classifier = LogisticRegression(max_iter=1000)
classifier.fit(X_train, y_train)

# Verifying model.
misidentified_examples = 0
for i in range(len(text_test)):
    if y_test[i] != classifier.predict(X_test[i]):
        misidentified_examples += 1
print("Number of errors: {}".format(misidentified_examples))
print("Accuracy on test data: {:.2f}%".format(100 - misidentified_examples * 100 / len(text_test)))
print("Accuracy on test data - method score: {:.2f}%".format(classifier.score(X_test, y_test) * 100))
print('Accuracy on train data - method score: {:.2f}%'.format(classifier.score(X_train, y_train) * 100))

scores = cross_val_score(classifier, X_train, y_train, cv=5)
print("Average correctness cross check: {:.2f}%".format(np.mean(scores) * 100))
