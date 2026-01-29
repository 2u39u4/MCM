import numpy as np

class WeightedModel:
    def __init__(self, weights):
        self.weights = weights

    def predict(self, X):
        w = np.array(list(self.weights.values()))
        return X @ w
