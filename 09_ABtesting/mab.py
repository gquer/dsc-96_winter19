
import numpy as np

class Simulator(object):
    
    def __init__(self, levers=10, seed=None):
        np.random.seed(seed)
        self.levers = levers
        self.probs = np.random.uniform(0.1, 0.4, size=levers)
        self.count = 0
        self.record = np.zeros(levers)
        self.success = np.zeros(levers)
        
    def pull(self, k):
        
        try:
            prob = self.probs[k]
            self.count += 1
            self.record[k] += 1
            if np.random.uniform() < prob:
                self.success[k] += 1
                return 1
            else:
                return 0
            
        except IndexError:
            print('That lever is out of range!')
            return
