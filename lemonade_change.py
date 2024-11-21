from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0] # 5, 10, 20
        
        #always give the customer the largest bills possible for change
        for bill in bills:
            if bill==5:
                change[0] += 1
            elif bill==10:
                change[1] += 1
                if change[0] == 0:
                    return False
                else:
                    change[0] -= 1
            else: # 20
                change[2] += 1
                if change[1] > 0:
                    change[1] -= 1
                    if change[0] > 0:
                        change[0] -= 1
                    else:
                        return False
                elif change[0] >= 3:
                    change[0] -= 3
                else:
                    return False
        return True


solution = Solution()
assert solution.lemonadeChange([5,5,5,10,20]) == True
assert solution.lemonadeChange([5,5,10,10,20]) == False