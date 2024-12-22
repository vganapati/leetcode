class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        
        pointer_0 = 0
        pointer_1 = 0

        chars = {}
        size_chars = 0
        max_len = 0

        while pointer_1 < len(s):
            
            new_char = s[pointer_1]
            if new_char in chars.keys():
                chars[new_char] += 1
            else:
                # move pointer_0 if needed
                while size_chars == k:
                    old_char = s[pointer_0]
                    if chars[old_char] == 1:
                        del chars[old_char]
                        size_chars -= 1
                    else:
                        chars[old_char] -= 1
                    pointer_0 += 1
                chars[new_char] = 1
                size_chars += 1
            pointer_1 += 1
            max_len = max(max_len, pointer_1 - pointer_0)
        return max_len

                    

solution = Solution()

s = "aac"; k = 1
assert solution.lengthOfLongestSubstringKDistinct(s,k) == 2

s = "eceba"; k = 2
assert solution.lengthOfLongestSubstringKDistinct(s, k) == 3

s = "aa"; k = 1
assert solution.lengthOfLongestSubstringKDistinct(s, k) == 2

