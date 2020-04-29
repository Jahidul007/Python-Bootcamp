def subUnsort(A):
    n = len(A)
    for i in range(0, n - 1):
        if A[i] > A[i + 1]:
            break
    if i == n - 1:
        return -1
    start = i
    for i in range(n - 1, start, -1):
        if A[i] < A[start] or A[i] < A[i - 1]:
            break
    end = i
    min = A[start]
    max = A[start]

    for i in range(start, end):
        if A[i] < min:
            min = A[i]
        if A[i] > max:
            max = A[i]
    for i in range (0, start):
        if A[i] > min:
            start = i
            break

    for i in range (n-1, end, -1):
        if A[i] < max:
            end = i
            break
    return [start,end]
 
print(subUnsort([2, 6, 4, 8, 10, 9, 15]))
