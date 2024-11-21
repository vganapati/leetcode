from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]):
        g.sort()
        s.sort()

        pointer_s = 0
        for ind, g_i in enumerate(g):
            while pointer_s < len(s) and g_i > s[pointer_s]:
                pointer_s += 1
            if pointer_s >= len(s):
                return ind
            elif g_i <= s[pointer_s]:
                # eat cookie
                pointer_s += 1
        return ind + 1

solution = Solution()
g = [1,2,3]; s = [1,1]
assert solution.findContentChildren(g,s) == 1

g = [1,2]; s = [1,2,3]
assert solution.findContentChildren(g,s) == 2