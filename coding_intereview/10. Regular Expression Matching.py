class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=None)
        def isMatchHelper(ptr_s, ptr_p):
            if ptr_p == len(p):
                return ptr_s == len(s)

            # If pattern pointer is at a dot or if the s and p match in this char
            first_match = ptr_s < len(s) and (p[ptr_p] == "." or s[ptr_s] == p[ptr_p])

            # If we are evaluating a * combination
            if ptr_p < len(p) - 1 and p[ptr_p + 1] == "*":
                # Check if one between these case has a match:
                # - No * match (thus we skip in ptr_p + 2 to skip char and *)
                # - single char match and then rest of s with same pattern (because of the *)
                return isMatchHelper(ptr_s, ptr_p + 2) or first_match and isMatchHelper(ptr_s + 1, ptr_p)

            # There was no * for this check, just check if there is a match between these chars and the all the nexts
            return first_match and isMatchHelper(ptr_s + 1, ptr_p + 1)

        return isMatchHelper(0, 0)