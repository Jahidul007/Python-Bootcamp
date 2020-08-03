class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        
        for key, group in itertools.groupby(chars):
            counter = len(list(group))
            chars[idx] = key
            if counter > 1:
                for c in str(counter):
                    idx += 1
                    chars[idx] = c
            idx += 1
        print(idx)
        return idx
