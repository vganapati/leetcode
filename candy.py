from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_vec = [1]*len(ratings)

        def forward_pass():
            for ind, rating in enumerate(ratings):
                if ind==0:
                    pass
                else:
                    if rating > ratings[ind-1]:
                        candy_vec[ind] = max(candy_vec[ind], candy_vec[ind-1] + 1)
        
        forward_pass()

        # backward pass
        candy_vec = candy_vec[::-1]
        ratings = ratings[::-1]

        forward_pass()

        return sum(candy_vec)


solution = Solution()
ratings = [1,0,2]
assert solution.candy(ratings) == 5 

ratings = [1,2,2]
assert solution.candy(ratings) == 4
