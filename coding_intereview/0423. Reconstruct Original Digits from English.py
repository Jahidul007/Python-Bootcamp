class Solution:
    def originalDigits(self, s: str) -> str:
        c, res = Counter(s), Counter()
        print(c)
        todo = [('g', 'eight', 8), ('x', 'six', 6), ('w', 'two', 2), ('z', 'zero', 0), ('t', 'three', 3), 
                ('r', 'four', 4), ('s', 'seven', 7), ('v', 'five', 5), ('i', 'nine', 9), ('o', 'one', 1)]

        for Id, w, n in todo:
            res[n] += c[Id]
            print(res)
            for ch in w:
                c[ch] -= res[n]

        return ''.join([str(n) * res[n] for n in range(10)])
