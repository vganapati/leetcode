from typing import List
from collections import defaultdict, deque

class Solution:
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda: None)
        def coinChange_i(coins: List[int], amount: int) -> int:
            if amount == 0:
                return 0
            num_coins_vec = []
            for coin in coins:
                if amount-coin >= 0:
                    if memo[amount-coin]:
                        num_coins = memo[amount-coin]
                    else:
                        num_coins = coinChange_i(coins, amount - coin)
                    if num_coins != -1:
                        num_coins_vec.append(num_coins + 1)
            if len(num_coins_vec)>0:
                output = min(num_coins_vec)
                memo[amount] = output
                return output
            else:
                memo[amount] = -1
                return -1
        return coinChange_i(coins, amount)
    
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        
        nodes = {}
        nodes_list = [amount]

        while len(nodes_list)>0:
            value = nodes_list.pop()
            children = []
            for coin in coins:
                new_val = value - coin
                if new_val >= 0:
                    if new_val in nodes.keys():
                        pass
                    else:
                        nodes_list.append(new_val)
                    children.append(new_val)
            nodes[value] = children

        if 0 not in nodes.keys():
            return -1 
        visited = set()
        nodes_list = set([amount])
        num_coins = 0

        while len(nodes_list)>0:
            num_coins += 1
            new_nodes_list = set()
            for value in nodes_list:
                visited.add(value)
                children = nodes[value]
                for child in children:
                    if child == 0:
                        return num_coins
                    if child in visited:
                        pass
                    else:
                        new_nodes_list.add(child)
            nodes_list = new_nodes_list
solution = Solution()

coins = [186,419,83,408]; amount=6249
assert solution.coinChange(coins, amount) == 20

coins = [1]; amount = 0
assert solution.coinChange(coins, amount) == 0

coins = [2]; amount = 3
assert solution.coinChange(coins, amount) == -1

coins = [1,5,10]; amount = 12
assert solution.coinChange(coins, amount) == 3

