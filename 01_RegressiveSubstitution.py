import numpy as np

def check_dimensions(A, b):
    '''A function that checks the dimensions of the input matrix and vector.
    Args:
        A (numpy.ndarray): A matrix of coefficients.
        b (numpy.ndarray): A vector of constants.'''
    
    A = np.asarray(A)
    b = np.asarray(b)

    if A.ndim != 2 or b.ndim != 1:
        raise ValueError("Input matrix must be 2-dimensional and vector must be 1-dimensional.")

    m, n = A.shape
    p = b.shape[0]

    if m != n:
        raise ValueError("Input matrix must be square.")
    if p != n:
        raise ValueError("Vector length must match the number of rows in the matrix.")

    return A,b

def gauss_elimination(A, b):
    '''A function that performs Gaussian elimination on a system of linear equations Ax = b.
    Args:
        A (numpy.ndarray): A matrix of coefficients.
        b (numpy.ndarray): A vector of constants.'''

    A,b = check_dimensions(A, b)
    n = A.shape[1]   
    Ab = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        for j in range(n):
            if j > i:
                if Ab[j][i] * Ab[i][i] + Ab[j][i] == 0:
                    Ab[j][:] = Ab[j][i] * Ab[i][:] + Ab[j][:]
                else:
                    Ab[j][:] = -(Ab[j][i] * Ab[i][:])/Ab[i][i] + Ab[j][:]
    
    return Ab[:, :-1], Ab[:, -1]

def regressive_substitution(A,b):
    '''A function that solves a system of linear equations Ax = b using regressive substitution.
    Args:
        A (numpy.ndarray): A superior triangular matrix of coefficients.
        b (numpy.ndarray): A vector of constants.'''
    
    A, b = check_dimensions(A, b)
    n = A.shape[1]

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

def regressive_substitution_2(A,b):
    '''
    A (numpy.ndarray): A superior triangular matrix of coefficients.
    b (numpy.ndarray): A vector of constants.'''
    
    A = np.asarray(A)
    b = np.asarray(b)
    
    if A.ndim != 2 or b.ndim != 1:
        raise ValueError("Input matrix must be 2-dimensional and vector must be 1-dimensional.")
    
    m, n = A.shape
    p = b.shape[0]
    
    if m != n:
        raise ValueError("Input matrix must be square.")
    if p != n:
        raise ValueError("Vector length must match the number of rows in the matrix.")

    if np.any(np.diag(A) == 0):
        raise ValueError("Matrix has a zero diagonal element.")

    for i in range(n):
        for j in range(i):
            if A[i][j] != 0:
                raise ValueError("Matrix is not superior triangular.")

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

    print("Algorith to perform regressive substitution from a superior triangular matrix.")
    print("Please enter the coefficients matrix A (Ex: [3, 1, -1], [0, 5, 1], [0, 0, 3]):")
    A = eval(input())
    print("Please enter the constants vector b (Ex: [2, 0, 4]):")
    b = eval(input())
    print("The solution is:")
    
    print(regressive_substitution_2(A, b))
