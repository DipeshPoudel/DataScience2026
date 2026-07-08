import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    """
    :param x1: New Data Point
    :param x2: Data Points in dataset
    :return: Distance between new data point and all data points in
    training set
    """
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance

# def euclidean_distance(x1, x2):
#     """
#     :param x1: New Data Point
#     :param x2: Data Points in dataset
#     :return: Distance between new data point and all data points in
#     training set
#     """
#     distance = np.linalg.norm(x1 - x2)
#     return distance    

class KNN:
    """
    KNN Class for implementing KNN Algorithm in Scikit-learn style
    """
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        """
        :param X: Feature Vector
        :param y: Class Label
        Sets the value of X_train and y_train.
        """

        self.X_train = X
        # [[1,20,20],[1,20,20]....]
        self.y_train = y

    def predict(self, X):
        """
        :param X: Datapoints for which prediction have to be made
        :return: Prediction for given datapoints 
        """
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        """
        Helper function that carries out actual prediction
        :param X: Datapoint for which prediction have to be made
        :return: Prediction for given datapoint 
        """
        # compute the distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
    
        # get the closest k
        k_indices = np.argsort(distances)[:self.k]
        # get First K labels
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]