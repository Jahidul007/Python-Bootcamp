def mysqrt(X):
    low = 0.0
    high = X
    for step in range(64):
        mid = (low + high) / 2
        if mid * mid > X:
            high = mid
        else:
            low = mid

    return mid


print(mysqrt(15))
