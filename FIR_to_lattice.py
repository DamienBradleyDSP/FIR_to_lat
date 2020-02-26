import numpy as np

def fir_to_lattice(inputCoeff):  # FIR coefficients must be normalised! (h[0] = 1)
    filterLength = len(inputCoeff)
    newCoeffs = np.zeros(filterLength-1)

    for i in range(0,filterLength-1):

        newCoeffs[-i-1] = inputCoeff[-1]                             # Latest element of k = last element of A
        imagePolynomial = np.flip(inputCoeff)                              # Make image polynomial
        inputCoeff = (1/(1-pow(newCoeffs[-i-1],2)))*(inputCoeff-newCoeffs[-i-1]*imagePolynomial)    # Apply recursive lattice equation
        inputCoeff = np.delete(inputCoeff,len(inputCoeff)-1)                   # Trim zero element at end of new array
    
    return newCoeffs


z = [1,0.2,-0.4,0.5]
k = fir_to_lattice(z)
print(k)

