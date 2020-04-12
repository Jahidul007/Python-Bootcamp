def power_root(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_root(x, -n)
    if n % 2 == 1:
        return x * power_root(x, n-1)
    pf = power_root(x, n / 2)

    return pf * pf


print(power_root(2, 10000000))
