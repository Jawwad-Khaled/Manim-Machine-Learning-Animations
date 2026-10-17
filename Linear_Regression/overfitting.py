import numpy as np

class Linear_Regression():
    def __init__(self):
        self.parameters = np.array([])
        
    def fit(self, X, y):
        self.parameters = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X):
        y_hat = X @ self.parameters
        return y_hat

np.random.seed(75)
x = 9 * np.random.rand(30)
y = 6 * x + 40 + 10 * np.random.randn(30)
y = np.clip(y, 0, 100)
X = np.hstack((np.ones_like(x.reshape(-1, 1)), x.reshape(-1, 1)))
X = np.hstack((X, x.reshape(-1, 1) ** -1, x.reshape(-1, 1) ** -2))
y = y.reshape(-1, 1)

linear_regression = Linear_Regression()
linear_regression.fit(X, y)
predictions = linear_regression.predict(X)
rmse = np.sqrt(np.mean((y - predictions)**2))
r2 = 1 - (np.sum((y - predictions)**2)) / (np.sum((y - np.mean(y))**2))
print(rmse)
print(r2)
print(linear_regression.parameters)