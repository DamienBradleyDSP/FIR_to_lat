import numpy as np

def fir_to_lattice(A):  # FIR coefficients must be normalised! (h[0] = 1)
    n = len(A)
    k = np.zeros(n-1)

    for i in range(0,n-1): #n-1

        k[-i-1] = A[-1]                             # Latest element of k = last element of A
        B = np.flip(A)                              # Make image polynomial
        A = (1/(1-pow(k[-i-1],2)))*(A-k[-i-1]*B)    # Apply recursive lattice equation
        A = np.delete(A,len(A)-1)                   # Trim zero element at end of new array
    
    return k


z = [1,0.2,-0.4,0.5]
k = fir_to_lattice(z)
print(k)

