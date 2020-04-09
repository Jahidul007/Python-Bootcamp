class solution:
    def max_distance(A):
        if len(A) < 2:
            return 0
        A.sort()
        pre = A[0]
        max_gap = float("-inf")

        for i in A:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap


print(solution.max_distance([3, 5, 4, 2]))
