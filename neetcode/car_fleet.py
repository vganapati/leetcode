from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass

solution = Solution()

target = 10; position = [1,4]; speed = [3,2]
assert solution.carFleet(target, position, speed) == 1

target = 10; position = [4,1,0,7]; speed = [2,2,1,1]
assert solution.carFleet(target, position, speed) == 3

