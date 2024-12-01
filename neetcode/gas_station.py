from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prefix = 0
        start_ind = 0
        max_gas = 0

        # total = []
        for ind, (g, c) in enumerate(zip(gas, cost)):
            total = g-c 
            # total.append(g - c)
            if prefix <= 0:
                prefix = 0
                start_ind_i = ind

            prefix += total

            if prefix >= max_gas:
                max_gas = prefix
                start_ind = start_ind_i
        breakpoint()
        
        # try start_ind


        return start_ind
 
        # for ind, t in enumerate(total):

solution = Solution()
gas = [1,2,3,4]; cost = [2,2,4,1]
assert solution.canCompleteCircuit(gas, cost) == 3

gas = [1,2,3]; cost = [2,3,2]
assert solution.canCompleteCircuit(gas, cost) == -1
