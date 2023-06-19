import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.txt")
X = df["temperature"]
y = df["humidity"]
model = LinearRegression()
model.fit(X, y)
m = model.coef_[0]
c = model.intercept_
print(f"Slope is {m} and intercept is {c}")
