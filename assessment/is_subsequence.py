class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0

        while pointer_t < len(t) and pointer_s < len(s):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        if pointer_s == len(s):
            return True
        return False

solution = Solution()
s = "abc"; t = "ahbgdc"
assert solution.isSubsequence(s, t) == True

s = "axc"; t = "ahbgdc"
assert solution.isSubsequence(s, t) == False