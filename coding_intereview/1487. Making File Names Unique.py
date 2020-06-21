class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nameMap = {}
        res = []

        for n in names:
            if n in nameMap:
                # find k
                k = nameMap[n] + 1
                while (n + "(" + str(k) + ")") in nameMap:
                    k += 1
                nameMap[n] = k
                n = n + "(" + str(k) + ")"

            nameMap[n] = 0
            res.append(n)
        return res
