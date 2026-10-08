import numpy as np

def resolve_lu(A, b):
    A = np.array(A, dtype=float)
    n = len(b)

    L = np.eye(n)

    # 1. Eliminação de Gauss: transforma A em U
    for i in range(n):

        if A[i, i] == 0:
            raise ValueError("Elemento nulo na diagonal de A. Escolha outro método de resolução.")

        for j in range(i + 1, n):
            fator = A[j, i] / A[i, i]
            L[j, i] = fator

            for k in range(i, n):
                A[j, k] -= fator * A[i, k]

    U = A

    # 2. Substituição progressiva: Ly = b
    y = np.zeros(n)

    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i, j] * y[j]

        # Não precisa da divisão por L[i, i] porque L é uma matriz triangular inferior com 1s na diagonal
        y[i] = b[i] - soma

    # 3. Substituição regressiva: Ux = y
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]

        x[i] = (y[i] - soma) / U[i, i]

    return L, U , x

if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)


    b = np.array([8, -11, -3], dtype=float)

    L, U , x = resolve_lu(A, b)

    print("Matriz L:")
    print(L)
    print("\nMatriz U:")
    print(U)
    print("\nSolução do sistema (x):")
    print(x)