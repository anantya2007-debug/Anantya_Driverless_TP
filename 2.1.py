def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements row by row for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Number of elements in row does not match columns.")
            return None
        matrix.append(row)
    return matrix

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        print("Error: Number of columns of A must equal number of rows of B.")
        return None

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

C = matrix_multiply(A, B)

print("Resultant Matrix C (A x B):", C)
