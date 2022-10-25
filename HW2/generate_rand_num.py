"""
This generates a list of random values between 0 and 1
Code can be found here:
https://github.com/ace15guest/ModernMaterials/tree/master/HW2
"""
import numpy as np

rand_list = np.random.rand(100)

print([round(x,2) for x in rand_list])