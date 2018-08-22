from sklearn.cluster import KMeans


class Miner:
    def __init__(self, n_groups=8, data=""):
        self.__n_groups = n_groups
        self.__data = data

    def mine(self):
        kmeans = KMeans(self.__n_groups, random_state=170)
