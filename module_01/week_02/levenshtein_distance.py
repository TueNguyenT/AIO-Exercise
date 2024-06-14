def levenshtein_distance(token1, token2):
    m = len(token1)
    n = len(token2)
    D = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        D[i][0] = i
    for j in range(n+1):
        D[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            v1 = D[i-1][j] + 1
            v2 = D[i][j-1] + 1
            v3 = D[i-1][j-1] + (token1[i-1] != token2[j-1])
            D[i][j] = min(v1, v2, v3)
    return D[m][n]


if __name__ == "__main__":
    print(levenshtein_distance('yu', 'you'))
    print(levenshtein_distance('hola', 'hello'))
