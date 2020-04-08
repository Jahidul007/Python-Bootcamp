def max_sum(arr):
    n = len(arr)
    max = 0
    for i in range(0, n):
        if arr[i] > max:
            max = arr[i]

        current_sum = arr[i]
        for j in range(i + 1, n):
            current_sum += arr[j]
            if current_sum > max:
                max = current_sum
    return max


print(max_sum([-1, -2, 1, 3, 2, -5, 4]))
