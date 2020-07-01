class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.",
                 "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        answer = set()
        word = ''
        for w in words:
            for i in w:
                word += morse[ord(i) - ord('a')]
            answer.add(word)
            word = ''
        return len(answer)
