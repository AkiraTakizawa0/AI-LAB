def apsp(matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix


if __name__ == "__main__":
    print("Enter number of nodes")
    n = int(input())
    m = []
    print("Enter Adjacency matrix")
    for i in range(n):
        row = []
        for j in range(n):
            c = int(input())
            row.append(c)
        m.append(row)
    matrix = apsp(m, n)
    print(f"Shortest path to all other nodes is ")
    for i in matrix:
        print(*i)