from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        prefix = 0
        start_ind = 0
        max_gas = 0

        output = []
        while start_ind < len(gas):
            ind = start_ind
            output.append(start_ind)
            prefix = gas[ind] - cost[ind]
            ind += 1
            while prefix > 0 and ind <= (start_ind + len(gas) - 1):
                if prefix >= max_gas:
                    max_gas = prefix
                    max_ind = start_ind
                prefix += gas[ind % len(gas)] - cost[ind % len(gas)]
                ind += 1
            start_ind = ind
        return output[-1]
 
solution = Solution()
gas = [5,8,2,8]; cost = [6,5,6,6]
assert solution.canCompleteCircuit(gas, cost) == 3

gas = [1,2,3,4]; cost = [2,2,4,1]
assert solution.canCompleteCircuit(gas, cost) == 3

gas = [1,2,3]; cost = [2,3,2]
assert solution.canCompleteCircuit(gas, cost) == -1
