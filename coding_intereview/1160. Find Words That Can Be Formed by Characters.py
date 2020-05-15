from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        for word in words:
            counter = 0
            for i in word:
                if word.count(i) <= chars.count(i):
                    counter += 1
                else:
                    break
            if counter == len(word):
                sum += len(word)
        return sum
