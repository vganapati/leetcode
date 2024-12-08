class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        start_ind = 0
        longest_substring = 0
        for ind,letter in enumerate(s):
            if letter in char_dict:
                start_ind = max(start_ind, char_dict[letter] + 1)
            char_dict[letter] = ind
            longest_substring = max(longest_substring, ind-start_ind+1)
        return longest_substring

            

solution = Solution()

s = "abba"
assert solution.lengthOfLongestSubstring(s) == 2

s = "zxyzxyz"
assert solution.lengthOfLongestSubstring(s) == 3

s = "xxxx"
assert solution.lengthOfLongestSubstring(s) == 1
