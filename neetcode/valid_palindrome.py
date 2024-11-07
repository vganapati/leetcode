class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        pointer_0 = 0
        pointer_1 = len(clean_s)-1

        while pointer_0 < pointer_1:
            if clean_s[pointer_0] != clean_s[pointer_1]:
                return False
            else:
                pointer_0 += 1
                pointer_1 -= 1
        return True

if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome("No lemon, no melon") == True
    assert solution.isPalindrome("Was it a car or a cat I saw?") == True
    assert solution.isPalindrome("tab a cat") == False
    
    print("All test cases passed!")