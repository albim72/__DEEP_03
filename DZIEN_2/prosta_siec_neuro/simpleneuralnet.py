import numpy as np

class SimpleNeuralNetwork:

    """
    Prosta sieć neuronowa która analizuje binarną reprezentację dodatniej liczby wejściowej
    """

    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1

    #funkcja aktywacji - sigmoid
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    #różniczka z funkcji aktywacji
    def d_sigmoid(self,x):
        return x*(1-x)

    def propagation(self,inputs):
        """
        proces propagacji
        """
        return self.sigmoid(np.dot(inputs.astype(float),self.weights))

    def backward_propagation(self,propagation_result,train_input,train_output):
        """
        proces propagacji wstecznej
        """
        error = train_output - propagation_result
        self.weights += np.dot(train_input.T,error*self.d_sigmoid(propagation_result))

    def train(self,train_input,train_output,train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backward_propagation(propagation_result,train_input,train_output)
