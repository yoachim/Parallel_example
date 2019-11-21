import numpy as np

class Example_object(object):
    " A simple class that can take in data and do some computation on it afterwards"
    def __init__(self):
        self.hw = "hello world!"
    def read_data(self, data):
        self.data = data
    def compute(self, scale):
        result = np.std(scale*self.data)
        return result

