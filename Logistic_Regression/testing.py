import numpy as np
import sklearn.linear_model as skl

np.random.seed(75)
x = 9 * np.random.rand(30)
X = x.reshape(-1, 1).copy()
for i in range(2, 11):
    X = np.hstack((X, x.reshape(-1, 1).copy() ** i))
y = 6 * x + 40 + 10 * np.random.randn(30)
y = np.clip(y, 0, 100)
y = [1 if item > 70 else 0 for item in y]

logistic_regression = skl.LogisticRegression(C=np.inf, max_iter=1000)
model = logistic_regression.fit(X, y)
predictions = logistic_regression.predict(X)
accuracy = np.sum(y == predictions) / len(y)
print(accuracy)
print(model.intercept_)
print(model.coef_)
