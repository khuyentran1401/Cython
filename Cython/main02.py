'''
Cython Documentation
https://cython.org/#documentation
http://docs.cython.org/en/latest/
'''

import numpy as np
from mult_fast import mulAB

if __name__=='__main__':

	A = np.loadtxt('./A.txt')
	B = np.loadtxt('./B.txt')

	result = mulAB(A ,B)
	print(result)