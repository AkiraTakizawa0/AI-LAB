import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

df = pd.read_csv("FiniteWords.csv", names=["Message", "label"])
df["target"] = df.label.map({"pos": 1, "neg": 0})
X = df["Message"]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)
model = MLPClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("*** Model Evaluation ***")
print(confusion_matrix(pred, y_test))
print(f"Accuracy is {accuracy_score(pred, y_test)}")