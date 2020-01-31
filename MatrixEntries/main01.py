import numpy as np
import time
import matplotlib.pyplot as plt


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

def npAB( A , B):
	C = A @ B
	return C


def calculate(func,dims):

        A = np.random.rand(dims[0],dims[1])
        np.savetxt('./A.txt', A)

        B = np.random.rand(dims[0],dims[1])
        np.savetxt('./B.txt', B)

        start_time=time.time()

        result = func(A ,B)

        end_time=time.time()

        secs = end_time -start_time

        return secs


if __name__=='__main__':

        nump= []
        mult=[]
        for i in range(0,500,100):
                nump.append(calculate(npAB,(i,i)))

                mult.append(calculate(mulAB,(i,i)))

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))

        x = np.arange(0,500,100)

        ax.plot(x,nump, color = 'blue', label = 'Numpy')
        ax.plot(x,mult, color = 'red', label = 'Multiplication')

        ax.set_xlabel('Dimension')
        ax.set_ylabel('Time (s)')

        ax.set_title('Numpy vs Multiplication')

        ax.legend(loc='upper left')

        ax.grid(b=True)

        fig.savefig("Numpy-Multiplication.png", dpi = 200)

        plt.show()
