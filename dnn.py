import numpy as np
from pprint import pprint

class DNN ():

    def __init__(self, shape, eta=1, n_epoch=100):

        self.eta = eta
        self.n_epoch = n_epoch
        self.shape = shape
        self.num_layers = len(shape)
        self.initialize(shape)


    def fit(self, X, y):
        X = np.array([np.append(i,[1]) for i in X])
        for _ in range(self.n_epoch):
            for x,y_ in zip(X,y):
                self.feed_foward(x)
                self.back_propagate(y_)

    def predict(self, X):

        X = np.array([np.append(i,[1]) for i in X])
        return self.feed_foward(X)
        #return [1 if i>=.5 else 0 for i in self.feed_foward(X)]

    def feed_foward(self, X):
        self.z[0] = X
        for i in range(1, self.num_layers):
            input = np.dot(self.z[i-1], self.w[i])
            self.z[i] = self.activation(input)
            self.act_prime[i] = self.activation_prime(input)
        return self.z[-1]

    def back_propagate(self, y):
        self.E[-1] = (self.z[-1] - y) * self.act_prime[-1]
        self.w[-1] += -self.eta * np.dot(np.atleast_2d(self.z[-2]).T, np.atleast_2d(self.E[-1]))
        for i in range(2,self.num_layers):
            self.E[-i] = np.dot(self.w[-i+1].T, self.E[-i+1]) * self.act_prime[-i]
            self.w[-i] += -self.eta * (np.dot(np.atleast_2d(self.z[-i-1]).T, np.atleast_2d(self.E[-i])))

    def activation(self, X):
        return 1 / (1+np.exp(-X))

    def activation_prime(self, X):
        return self.activation(X)*(1-self.activation(X))

    def initialize(self, shape):

        shape = [i+1 for i in shape[:-1]] + [shape[-1]]
        print('shape:',shape,'\n')

        # initialize weights
        self.w = []
        self.w.append([])
        for i in range(1,len(shape)):
            self.w.append(np.ones((shape[i-1],shape[i])))#np.random.uniform(-1,1,(shape[i-1], shape[i])))

        # initialize phi', output (z)
        self.z, self.act_prime, self.E = [], [], []
        for i in shape:
            self.z.append(np.zeros((i,1)))
            self.act_prime.append(np.zeros((i,1)))
            self.E.append(np.zeros((i,1)))


# # X = np.array([[1,1],[0,0],[1,0],[0,1]])
# # y = np.array([[1],[0],[0],[0]])
# X = np.array([[1,1],[0,0],[1,0],[1,1],[0,1],[1,1]])
# y = np.array([[1],[0],[0],[1],[0],[1]])
# d = dnn(shape=[2,2,1])
# d.fit(X,y)
#
# p = d.predict(X)
# print(p)