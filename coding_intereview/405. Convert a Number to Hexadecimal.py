class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num > 0:
            return hex(num).lstrip("0x")
        else:
            return hex((num + (1 << 32)) % (1 << 32)).lstrip("0x")
