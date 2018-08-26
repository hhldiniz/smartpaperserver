import numpy
from sklearn.cluster import KMeans


class Miner:
    def __init__(self, n_groups=8, data=None, dtype=object, categories=None):
        if categories is None:
            categories = []
        if data is None:
            data = []
        self.__n_groups = n_groups
        self.__categories = categories
        self.__data = numpy.array(data, dtype=dtype)

    def mine(self):
        kmeans = KMeans(self.__n_groups, random_state=170)
        print(self.__data)
        return kmeans.fit(self.__data.reshape(-1, 1))
