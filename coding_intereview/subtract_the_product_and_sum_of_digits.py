class Solution:
    def subtractProductAndSum(self, n: List[int]) -> int:
        number = [int(i) for i in str(n)]
        product = 1
        add = 0
        print(number)
        for i in range(len(number)):
            product *= number[i]
            add += number[i]
            print(product)
        result = product - add
        return result

