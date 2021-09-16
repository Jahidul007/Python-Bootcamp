class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if(ch in word):
            return ch+word.split(ch, 1)[0][::-1]+word.split(ch, 1)[1]
        else:
            return word
