class Solution(object):
    def letterCombinations(self, digits):
        """7
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','0'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        n = len(digits)
        result = []
        def recurse(i, li):
            if len(li) == n:
                result.append("".join([x for x in li]))
                return
            for ch in digit_map[digits[i]]:
                li.append(ch)
                recurse(i+1, li)
                li.pop()
        recurse(0,[])
        return result
print(Solution().letterCombinations('22'))