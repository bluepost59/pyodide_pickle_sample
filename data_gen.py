import json

import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


def main():
    shape = (100, 5)

    xx = np.ones(shape)+np.random.random(shape)

    scaler = StandardScaler().fit(xx)

    # json.dump(scaler, "test.json")
    with open("scaler.pkl", mode="wb") as f:
        pickle.dump(scaler, f)

    print(scaler.transform(np.array([[1, 2, 3, 4, 5]]))),


if __name__ == "__main__":
    main()
