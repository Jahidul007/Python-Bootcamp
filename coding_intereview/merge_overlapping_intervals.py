def merge(intervals):
    intervals.sort()
    n = len(intervals)
    new_intervals = []
    if n != 0:
        new_intervals.append(intervals[0])

        for i in range(1, n):
            start, end = new_intervals[-1]

            if intervals[i][0] > end:
                new_intervals.append(intervals[i])
            elif intervals[i][1] > end:
                end = intervals[i][1]
                new_intervals[-1] = (start, end)
    return new_intervals


print(merge([(1, 3), (2, 6), (8, 10), (15, 18)]))
