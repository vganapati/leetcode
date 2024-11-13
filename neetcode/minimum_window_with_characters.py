from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c] += 1
        
        total_count = 0
        pointer_0 = 0
        min_string = [float("inf"), 0, 0]
        letter_array = []

        flag = True
        for pointer_1, c in enumerate(s):
            if c in t_dict:
                if flag: # move pointer_0 to the first included letter
                    pointer_0 = pointer_1
                    flag = False
                letter_array.append([c, pointer_1])
                t_dict[c] -= 1
                if t_dict[c] >= 0:
                    total_count += 1
                    if total_count == len(t):
                        if min_string[0] > (pointer_1 - pointer_0)+1:
                            min_string = [(pointer_1 - pointer_0)+1, pointer_0, pointer_1]
                else: # gone negative for the letter, move pointer_0 to the right as much as possible
                    i = 0
                    for i, [letter, position] in enumerate(letter_array):
                        if t_dict[letter] < 0:
                            t_dict[letter] += 1
                        else:
                            break
                    letter_array = letter_array[i:]
                    pointer_0 = letter_array[0][1] # move pointer_0
                    if total_count == len(t): # update min_string
                        if min_string[0] > (pointer_1 - pointer_0)+1:
                            min_string = [(pointer_1 - pointer_0)+1, pointer_0, pointer_1]
        if min_string[0] == float("inf"):
            return ""
        else:
            return s[min_string[1]:min_string[2]+1]

if __name__ == "__main__":
    solution = Solution()

    s = "aaaaaaaaaaaabbbbbcdd"; t = "abcdd"
    assert solution.minWindow(s,t) == "abbbbbcdd"

    s = "OUZODYXAZV"; t = "XYZ"
    assert solution.minWindow(s,t) == "YXAZ"

    s = "xyz"; t = "xyz"
    assert solution.minWindow(s,t) == "xyz"

    s = "x"; t = "xy"
    assert solution.minWindow(s,t) == ""
