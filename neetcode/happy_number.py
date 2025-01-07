class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = set()

        while True:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            
            n = sum
            if n == 1:
                return True
            if n in prev_nums:
                return False

            prev_nums.add(n)

solution = Solution()
assert solution.isHappy(19) == True
assert solution.isHappy(100) == True
assert solution.isHappy(101) == False
