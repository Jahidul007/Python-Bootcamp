class Solution(object):
    def isNumber(self, s):
        s = s.strip()       # delete all space in front and rear of string
        if ' ' in s:
            return False    # return false if there is any space in string's middle

        # check the front and back parts of 'e' separately
        if 'e' in s:
            return self.isNumberFront(s.partition('e')[0]) and self.isNumberBack(s.partition('e')[2])
        else:
            return self.isNumberFront(s)

    def isNumberFront(self, s1):
        if not s1 or (s1[0] == 0 and s1[1] != '.') or '-' in s1[1:] or '+' in s1[1:]:
            return False
        if (s1[0] == '-' or s1[0] == '+' or s1 == '.') and len(s1) == 1:  # if only 1 character and it is not an integer
            return False
        for c in s1:
            if c != '+' and c != '.' and c != '-' and not ord('0') <= ord(c) <= ord('9'):
                return False
            if c == '.':
                dot_index = s1.index('.')
                if len(s1)-1 > dot_index:
                    if '.' in s1[dot_index + 1:]:
                        return False
                elif not ord('0') <= ord(s1[dot_index-1]) <= ord('9'):
                    return False
        return True

    def isNumberBack(self, s2):
        if not s2 or '-' in s2[1:] or '+' in s2[1:]:
            return False
        if s2[0] == '-' or s2[0] == '+':
            if len(s2) == 1:
                return False
            elif s2[1] == 0:
                return False
        for c in s2:
            if not ord('0') <= ord(c) <= ord('9') and c != '+' and c != '-':
                return False
        return True


print(Solution().isNumber('3.'))
