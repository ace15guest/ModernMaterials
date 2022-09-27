"""
This generates a list of random values between 0 and 1

"""
import numpy as np

rand_list = np.random.rand(100)

print([round(x,2) for x in rand_list])