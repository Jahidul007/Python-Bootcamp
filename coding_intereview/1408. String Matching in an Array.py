class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        newlist = []
        for i in range(len(words)):
            temp = copy.deepcopy(words)
            temp.remove(words[i])
            for j in range(len(words) - 1):
                if words[i] in temp[j]:
                    newlist.append(words[i])
        return list(set(newlist))
