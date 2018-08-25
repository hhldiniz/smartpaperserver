import numpy
from sklearn.cluster import KMeans


class Miner:
    def __init__(self, n_groups=8, data=None):
        if data is None:
            data = []
        self.__n_groups = n_groups
        self.__data = numpy.array(data)

    def mine(self):
        kmeans = KMeans(self.__n_groups, random_state=170)
        return kmeans.fit(self.__data.reshape(-1, 1))
