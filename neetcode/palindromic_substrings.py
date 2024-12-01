"""
https://neetcode.io/problems/palindromic-substrings
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for ind in range(len(s)):
            # odd length
            left, right = ind, ind
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -=  1
                right += 1
            # even length
            if (ind+1) < len(s):
                left, right = ind, ind+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        count += 1
                    else:
                        break
                    left -=  1
                    right += 1
        return count


solution = Solution()
s = "abc"
assert solution.countSubstrings(s)==3

s = "aaa"
assert solution.countSubstrings(s)==6

