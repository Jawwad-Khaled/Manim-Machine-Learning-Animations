import numpy as np
import sklearn.linear_model as skl

np.random.seed(75)
x = 9 * np.random.rand(30)
y = 2 + 7 * np.random.rand(30)
X = np.hstack((np.ones((30, 1)), x.reshape(-1, 1).copy(), y.reshape(-1, 1).copy()))
z = 4 * x + 2 * y + 40 + 10 * np.random.randn(30)
z = np.clip(z, 0, 100)
z = [1 if item > 70 else 0 for item in z]

linear_regression = skl.LinearRegression()
model = linear_regression.fit(X, z)
parameters_linear = model.coef_
print(parameters_linear)

logistic_regression = skl.LogisticRegression(C=np.inf)
model = logistic_regression.fit(X, z)
parameters_logistic = model.coef_
print(parameters_logistic)
