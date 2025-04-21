# Matrix Ai has dimension arr[i-1] x arr[i]
def minMultRec(arr, i, j):

    # If there is only one matrix
    if i + 1 == j:
        return 0

    res = sys.maxsize

    # Place the first bracket at different
    # positions or k and for every placed
    # first bracket, recursively compute
    # minimum cost for remaining brackets
    # (or subproblems)
    for k in range(i + 1, j):
        curr = minMultRec(arr, i, k) \
            + minMultRec(arr, k, j) \
            + arr[i] * arr[k] * arr[j]

        res = min(curr, res)

    # Return minimum count
    return res


def matrixMultiplication(arr):
    n = len(arr)
    return minMultRec(arr, 0, n - 1)


if __name__ == "__main__":
    arr = [2, 1, 3, 4]
    res = matrixMultiplication(arr)
    print(res)
