def create_cubes(n):
    result = []

    for x in range(n):
        result.append(x**3)
    return result
print(create_cubes(5))