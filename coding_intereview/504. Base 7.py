class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = ''
        if num < 0:
            sign = '-'
            num = -num
        base7_list = []
        while num > 0:
            base7_list = [str(num % 7)] + base7_list
            num //= 7
        return sign + ''.join(base7_list)