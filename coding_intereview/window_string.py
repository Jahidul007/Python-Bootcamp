from collections import Counter, defaultdict
class Solution:
    def minWindow(self,S, T):
        t_freq = Counter(T)
        different_chars = len(t_freq)

        s_freq = defaultdict(int)

        len_s = len(S)
        min_left, min_right, min_len = -1, -1, len_s + 1

        matched = 0

        left = 0
        for right in range(len_s):
            ch_add = S[right]
            s_freq[ch_add] += 1
            if ch_add in t_freq and s_freq[ch_add] == t_freq[ch_add]:
                matched += 1

            while matched == different_chars and left <= right:
                ch_remove = S[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left, min_right = left, right

                s_freq[ch_remove] -= 1
                if ch_remove in t_freq and s_freq[ch_remove] < t_freq[ch_remove]:
                    matched -= 1

                left += 1

        if min_len == len_s + 1:
            return ""

        return S[min_left:min_right + 1]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
