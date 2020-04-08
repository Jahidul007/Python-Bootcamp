def max_sum(arr):
    n = len(arr)
    max = arr[0]
    current_sum = 0
    for i in range(0, n):
        current_sum += arr[i]
        if max < current_sum:
            max = current_sum
        if current_sum < 0:
            current_sum = 0
    return max


print(max_sum([-2, -1, 2, 1, 3, -5, 4]))
