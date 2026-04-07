from sklearn.linear_model import LinearRegression

class Model:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)
