import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("RestaurantReviews.tsv", skiprows=0, sep="\t")
X = df["Review"]
y = df["Liked"]

X_train, X_test, y_train, y_test = train_test_split(X, y)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)
model = MultinomialNB()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("*** Evaluation ***")
print(confusion_matrix(pred, y_test))
print(f"Accuracy is {accuracy_score(pred, y_test)}")
