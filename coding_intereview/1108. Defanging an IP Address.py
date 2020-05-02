class Solution:
    def defangIPaddr(self, address: str) -> str:
        newad = []
        for i in range(len(address)):
            if address[i]=='.':
                newad.append("[.]")
            else:
                newad.append(address[i])
        return "".join(newad)