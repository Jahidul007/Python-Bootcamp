import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your knn and naive bayes structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            self.max_heap.append(-num)
            return
        if len(self.min_heap) ==0:
            if num< -self.max_heap[0]:
                max_n = -heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)
                self.min_heap.append(max_n)
            else:
                self.min_heap.append(num)
            return
        if num <= self.min_heap[0]:
            if len(self.max_heap) <= len(self.min_heap):
                heapq.heappush(self.max_heap, -num)
            else:
                if num >= -self.max_heap[0]:
                    heapq.heappush(self.min_heap, num)
                else:
                    max_n = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.max_heap, -num)
                    heapq.heappush(self.min_heap, max_n)
        else:
            if len(self.max_heap) >= len(self.min_heap):
                heapq.heappush(self.min_heap, num)
            else:
                min_n = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -min_n)

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return self.min_heap[0]

if __name__ == "__main__":
    mf = MedianFinder()

    for num in [1, 3, 2, 6, 7, 4, 5, 9, 10]:
        mf.add_num(num)
        print(mf.find_median())

    for num in [-1, -2, -3, -4, -5]:
        mf.add_num(num)
        print(mf.find_median())
