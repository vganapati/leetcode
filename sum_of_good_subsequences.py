from typing import List
import collections
from collections import defaultdict

class TreeNode:
    def __init__(self, val, parent = None, first_tree=True, cum_sum=None, depth=1):
        self.val = val
        self.parent = parent
        self.first_tree = first_tree
        self.children = []
        if cum_sum == None:
            self.cum_sum = val
        else:
            self.cum_sum = cum_sum 
        self.depth = depth

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        nums_hash = defaultdict(lambda: [0,0])
        running_total = 0
        for num in nums:
            prev_sum_0, num_occurances_0 = nums_hash[num - 1]
            prev_sum_1, num_occurances_1 = nums_hash[num + 1]

            curr_sum = num + (prev_sum_0 + num_occurances_0*num) + (prev_sum_1 + num_occurances_1*num) 
            nums_hash[num][0] += curr_sum
            nums_hash[num][1] += 1 + num_occurances_0 + num_occurances_1
            running_total += curr_sum
            running_total = running_total % (10**9 + 7)
        return running_total

    def sumOfGoodSubsequences_0(self, nums: List[int]) -> int:
        trees = []
        cum_sum = 0
        for num in nums:
            flag = False # haven't added num to any existing tree
            first_tree = True
            for root_node in trees:
                # add num as a child node wherever the parent is +- 1
                # each time num is added as a child, add the value of num to cum_sum
                node_list = collections.deque([root_node])
                while len(node_list) > 0:
                    curr_node = node_list.popleft()
                    for child in curr_node.children:
                        node_list.append(child)
                    if abs(curr_node.val - num) == 1:
                        flag = True
                        if first_tree:
                            depth = curr_node.depth + 1
                        else:
                            depth = curr_node.depth
                        newNode_cum_sum = curr_node.cum_sum + depth*num
                        newNode = TreeNode(num, curr_node, first_tree, newNode_cum_sum, depth)
                        curr_node.children.append(newNode)

                        cum_sum += newNode_cum_sum
                        # print(newNode_cum_sum)
                        cum_sum = cum_sum % (10**9 + 7)

                        # curr_node_2 = newNode
                        # cum_sum_2 = 0
                        # i = 0
                        # while curr_node_2 is not None:
                        #     cum_sum_2 += curr_node_2.val
                        #     if curr_node_2.first_tree:
                        #         # print(cum_sum_2)
                        #         cum_sum += cum_sum_2
                        #         cum_sum = cum_sum % (10**9 + 7)
                        #     curr_node_2 = curr_node_2.parent
                        #     i += 1
                        first_tree = False
            # add num as the root of a new tree if flag is False
            if not(flag):
                trees.append(TreeNode(num))
                # print(num)
                cum_sum += num
                cum_sum = cum_sum % (10**9 + 7)
        # breakpoint()
        return cum_sum

if __name__ == "__main__":
    solution = Solution()
    assert solution.sumOfGoodSubsequences([3,3,4,3]) == 54
    assert solution.sumOfGoodSubsequences([3,1,2,9]) == 23
    assert solution.sumOfGoodSubsequences([1,2,1]) == 14
    assert solution.sumOfGoodSubsequences([3,4,5]) == 40