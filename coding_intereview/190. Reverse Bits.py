class Solution:
    def reverseBits(self, n: int) -> int:
        bin_number = bin(n)
        reverse_number = bin_number[-1:1:-1]
        reverse_number = reverse_number + (32 - len(reverse_number))*'0'
        return int(reverse_number,2)