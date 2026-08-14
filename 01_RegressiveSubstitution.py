import numpy as np

def gauss_elimination(A, b):
    '''A function that performs Gaussian elimination on a system of linear equations Ax = b.
    Args:
        A (numpy.ndarray): A matrix of coefficients.
        b (numpy.ndarray): A vector of constants.'''
    
    A = np.asarray(A)
    b = np.asarray(b)

    if A.ndim != 2 or b.ndim != 1:
        raise ValueError("Input matrix must be 2-dimensional and vector must be 1-dimensional.")

    m, n = A.shape

    if m != n:
        raise ValueError("Input matrix must be square.")

    Ab = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        for j in range(n):
            if j > i:
                if Ab[j][i] * Ab[i][i] + Ab[j][i] == 0:
                    Ab[j][:] = Ab[j][i] * Ab[i][:] + Ab[j][:]
                else:
                    Ab[j][:] = -Ab[j][i] * Ab[i][:] + Ab[j][:]
    
    return Ab[:, :-1], Ab[:, -1]

def regressive_substitution(A,b):
    '''A function that solves a system of linear equations Ax = b using regressive substitution.
    Args:
        A (numpy.ndarray): A superior triangular matrix of coefficients.
        b (numpy.ndarray): A vector of constants.'''
    
    A = np.asarray(A)
    b = np.asarray(b)

    if A.ndim !=2  or b.ndim != 1:
        raise ValueError("Input matrix must be 2-dimensional and vector must be 1-dimensional.")

    m,n = A.shape

    if m!=n:
        raise ValueError("Input matrix must be square.")

    x = np.zeros(n)
    c = np.zeros(n)

    for i in range(n-1, -1, -1):
        if i == n-1:
            x[i] = b[i]/A[i][i]
        else:
            for j in range(i,n-1):
                c[i] += A[i][j+1]*x[j+1]
            x[i] = (b[i] - c[i])/A[i][i]
    
    return x

if __name__ == "__main__":
    A = [[1, 1, -1], [2, 1, 1], [-1, -2, 3]]
    b = [2, 0, 4]

    superior_triangular, vector = gauss_elimination(A, b)
    print(regressive_substitution(superior_triangular, vector))