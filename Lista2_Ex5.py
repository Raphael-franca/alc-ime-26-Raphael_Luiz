import numpy as np

def check_dimensions(A):
    if A.ndim != 2:
        raise ValueError("Input a 2 dimensional matrix")
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

def is_orthogonal_by_definition(A):
    check_dimensions(A)
    if np.allclose(np.dot(A.T,A), np.eye(np.size(A,0)), atol=TOL):
        return True
    else:
        return False

def is_orthogonal_by_vectors(A):
    check_dimensions(A)
    n = A.shape[0]

    #Check if norm of each vector is 1
    for i in range(n):
        if not np.allclose(np.linalg.norm(A[i,:]), 1, atol=TOL):
            return False

    #Check if all vectors are orthogonal to each other
    for i in range(n):
        for j in range(i+1,n):
            if not np.allclose(np.dot(A[i,:],A[j,:]), 0, atol = TOL):
                return False
    return True

def display_result(A):
    if is_orthogonal_by_definition(A):
        print("Matrix is orthogonal by definition")
    else:
        print("Matrix is not orthogonal by definition")
    if is_orthogonal_by_vectors(A):
        print("Matrix is orthogonal by vectors")   
    else:
        print("Matrix is not orthogonal by vectors")

if __name__ == "__main__":
    TOL = 1e-4
    P1 = np.array([[-0.40825, 0.43644, 0.80178],[-0.8165, 0.21822, -0.53452],[-0.40825, -0.87287, 0.26726]])
    P2 = np.array([[-0.51450, 0.48507, 0.70711],[-0.68599, -0.72761, 0.0000],[0.51450, -0.48507, 0.70711]])
    P1_2 = np.array([[-0.58835, 0.70206, 0.40119],[-0.78446, -0.37524, -0.49377],[-0.19612, -0.60523, 0.77152]])
    P2_2 = np.array([[-0.47624, -0.4264, 0.30151], [0.087932, 0.86603, -0.40825], [-0.87491, -0.26112, 0.86164]])
    ss

    display_result(P1)
    display_result(P2)
    display_result(P1_2)
    display_result(P2_2)
    