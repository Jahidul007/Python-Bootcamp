def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ");
    print("")
    return


# The core function that recursively
# generates and prints all sequences  
# of length k  
def printSequencesRecur(arr, n, k, index):
    if (k == 0):
        printArray(arr, index)

    if (k > 0):
        for i in range(1, n + 1):
            arr[index] = i
            printSequencesRecur(arr, n, k - 1,
                                index + 1)

        # A function that uses printSequencesRecur() to


# prints all sequences from 1, 1, ..1 to n, n, ..n
def printSequences(n, k):
    arr = [0] * n
    printSequencesRecur(arr, n, k, 0)

    return;


# Driver Code
n = 5
k = 6
printSequences(n, k)