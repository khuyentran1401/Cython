# cython: cdivision=True
# cython: boundscheck=False
# cython: wraparound=False
# cython: infer_types=True

cimport cython
import numpy as np

def mulAB( double[:,:] A , double[:,:] B):

	cdef int Am  = A.shape[0]
	cdef int An  = A.shape[1]
	cdef int Bm  = B.shape[0]
	cdef int Bn  = B.shape[1]

	cdef int i = 0
	cdef int j = 0
	cdef int k = 0

	cdef double temp = 0.0

	cdef double[:,:] C = np.empty((Am,Bn), dtype=np.double)

	with nogil:
		for i in range(Am):
			for j in range(Bn):
				temp=0.0
				for k in range(An):
					temp += A[i,k] * B[k,j] 
				C[i,j] = temp
	
	return np.array(C)