import re


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = re.sub("[^\w]", " ", sentence).split()
        for i in lst:
            if searchWord in i and searchWord[0] == i[0]:
                return lst.index(i) + 1

        return -1
