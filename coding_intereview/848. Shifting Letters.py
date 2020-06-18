class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        st = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
        print(len(st))
        ans = list(S)
        current = sum(shifts)
        for i in range(len(S)):
            index = (current + st.index(S[i])) % 26
            ans[i] = (st[index])
            current -= shifts[i]

        return "".join(ans)
