import numpy as np


def mulAB( A , B):
	C = A @ B
	return C



if __name__=='__main__':
	
	# Create matrix
	
	A = np.random.rand(500,500)
	np.savetxt('./A.txt', A)

	B = np.random.rand(500,500)
	np.savetxt('./B.txt', B)
	

	#result = sumaAB(A,B)
	result = mulAB(A,B)
	print(result)