class KNN:
    k = 0
    data = None
    labels = None
    
    def __init__(self, k):
        self.k = k
        
    def train(self, vals, labs):
        self.data = vals
        self.labels = labs
    
    def predict(self, X):
        
        #make sure columns equal
        #assert(self.data.shape[1] == (len(X[i]) for i in X)) # will come back to this
        #assert(self.data.shape[1] == len(X[0]))
        
        dist = [
            (self.labels[i], la.norm(X-self.data[i])) for i in range(len(data))
        ]
        
        k_nearest = sorted(dist, key = lambda X: X[1])
        k_nearest = k_nearest[:self.k]

        f = c([p[0] for p in k_nearest])
        return f
