import numpy as np


def mulAB( A , B):

	(Am, An) = A.shape
	(Bm, Bn) = B.shape

	C = np.empty( (Am,Bn))

	for i in range(Am):
		for j in range(Bn):
			temp=0.0
			for k in range(An):
				temp += A[i,k] * B[k,j] 
			C[i,j] = temp
	
	return C



if __name__=='__main__':
	
	# Create matrix
	'''
	A = np.random.rand(500,500)
	np.savetxt('./A.txt', A)

	B = np.random.rand(500,500)
	np.savetxt('./B.txt', B)
	'''

	A = np.loadtxt('./A.txt')
	B = np.loadtxt('./B.txt')

	result = mulAB(A,B)
	print(result)