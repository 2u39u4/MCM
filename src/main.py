from models.weighted import WeightedModel
from config import WEIGHTS
import numpy as np

if __name__ == "__main__":
    X = np.array([
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ])

    model = WeightedModel(WEIGHTS)
    scores = model.predict(X)

    print("Model output:", scores)
