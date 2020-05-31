class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        num = [0] * (n + 1)
        for i, j, k in bookings:
            num[i - 1] += k
            num[j] += -k
        for i in range(1, n):
            num[i] += num[i - 1]
        return num[:-1]