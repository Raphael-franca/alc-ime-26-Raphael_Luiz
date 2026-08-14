import numpy as np

def matrix_product(A, B):
    A = np.asarray(A)
    B = np.asarray(B)
    
    if A.ndim !=2 or B.ndim != 2:
        raise ValueError("Input matrices must be 2-dimensional.")
    
    m, n = A.shape
    p, q = B.shape

    if n != p:
        raise ValueError("Inner dimensions must match for matrix multiplication.")
    
    return A @ B

def gauss_elimination(A):
    A = np.asarray(A)

    if A.ndim!=2:
        raise ValueError("Input matrix must be 2-dimensional.")

    m, n = A.shape

    if m!=n:
        raise ValueError("Input matrix must be square.")

    for i in range(n):
        for j in range (n):
            if j>i:
                A[j][:]=(-A[j][i])*A[i][:]+A[j][:]
    return A


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    C = [[1, 1, -1], [2, 1, 1], [-1, -1, 3]]
    
    print(f"Matrix A: {A}")
    print(f"Matrix B: {B}")
    print(f"A.B: {matrix_product(A, B)}")
    print(f'Matrix C: {C}')
    print(f'Gauss elimination of C: {gauss_elimination(C)}')