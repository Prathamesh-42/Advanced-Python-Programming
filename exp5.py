def LCS(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0

            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1

            else:
                lcs_table[i][j] = max(
                    lcs_table[i - 1][j],
                    lcs_table[i][j - 1]
                )

    # Length of LCS
    index = lcs_table[m][n]

    # Create LCS string
    lcs_string = [""] * index

    i = m
    j = n

    # Backtracking to find actual LCS
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return "".join(lcs_string), lcs_table[m][n]


# Main program
X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

lcs, length = LCS(X, Y)

print("Longest Common Subsequence:", lcs)
print("Length of LCS:", length)