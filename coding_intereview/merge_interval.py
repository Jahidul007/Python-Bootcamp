def insert(intervals, new_interval):
    n = len(intervals)

    start, end = 0, 0
    while end < n:
        if new_interval[0] <= intervals[end][1]:
            if new_interval[1] < intervals[end][0]:
                break
            new_interval[0] = min(new_interval[0], intervals[end][0])
            new_interval[1] = max(new_interval[1], intervals[end][1])

        else:
            start += 1
        end += 1
    return intervals[:start] + [new_interval] + intervals[end:]

intervals = [[5, 8], [9, 11]]
new_interval = [1, 3]
merged_interval = insert(intervals, new_interval)
print(merged_interval)