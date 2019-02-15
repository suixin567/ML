import numpy as np

a = np.zeros((4,5))
b = np.zeros((4,5))
c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
d = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
print(c.shape);
print(d.shape);
e = np.convolve(c,d,'same')
print(e);