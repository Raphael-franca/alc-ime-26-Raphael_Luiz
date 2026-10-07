import numpy as np

def eschelon(A):

    A = A.astype(float)
    n = A.shape[1]
    pivot_row = 0

    for i in range(n):
        if pivot_row >= n:
            break

        max_row = np.argmax(np.abs(A[pivot_row:, i])) + pivot_row

        if abs(A[max_row,i]) < 1e-12:
            continue

        if max_row != pivot_row:
            A[[pivot_row, max_row]] = A[[max_row, pivot_row]]

        for j in range(pivot_row + 1, n):
            A[j,:] -= (A[j,i] * A[pivot_row,:])/A[pivot_row,i]
        pivot_row += 1
    
    return A

def rank(A):
    eschelon_A = eschelon(A)
    return np.sum(np.any(np.abs(eschelon_A) > 1e-12, axis=1))

def norm2(v):
    return np.sqrt(np.sum(np.abs(v)**2))


for n in [5,15,25]:

    u = 10*np.random.rand(n)
    v = 10*np.random.rand(n)
    
    u = u.reshape(n,1)
    v_T = v.reshape(1,n)
    uv_T = np.dot(u,v_T)

    print("n: ", n)
    print(f"rank(uv^T): {rank(uv_T)}")
    print(f"rank(uv^T): {np.linalg.matrix_rank(uv_T)}")
    print(f"||u|| ||v||: {norm2(u)*norm2(v)}")
    print(f"||u||*||v||: {np.linalg.norm(u)*np.linalg.norm(v)}")
    print(f"||uv^T||: {np.linalg.norm(uv_T, ord=2)}")
    print(np.dot(np.transpose(uv_T),uv_T))

    

