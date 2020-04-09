def hotel_booking(arrive, depart, k):
    n = len(arrive)
    i, j = 0, 0
    arrive.sort()
    depart.sort()
    count = 0
    while i < n and j < n:
        if arrive[i] < depart[j]:
            count += 1
            if count > k:
                return False
            i += 1
        else:
            count -= 1
            j += 1
    return True


arrivals = [1, 3, 7]
departs = [2, 6, 8]
k = 1
print(hotel_booking(arrivals, departs, k))
