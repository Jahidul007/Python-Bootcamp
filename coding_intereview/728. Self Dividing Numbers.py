class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        divlist = []
        for i in range(left, right + 1, +1):
            if self.isDividingNumber(i):
                divlist.append(i)
        return divlist
