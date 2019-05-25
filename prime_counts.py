def prime_count(num):
    if num < 2:
        return 0
    # store our prime sumber
    primes = [2]
    x = 3
    # x is going through every number up to input num
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
print(prime_count(100))
