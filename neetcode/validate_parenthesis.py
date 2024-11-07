class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            # if open p, add to stack
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else: # close p
                if len(stack)>0:
                    last_p = stack.pop()
                    # Check if last_p closes p
                    if last_p == "(" and p == ")":
                        pass
                    elif last_p == "[" and p == "]":
                        pass
                    elif last_p == "{" and p == "}":
                        pass
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("[") == False
    assert solution.isValid("[]") == True
    assert solution.isValid("([{}])") == True
    assert solution.isValid("[(])") == False
    print("All test cases passed!")