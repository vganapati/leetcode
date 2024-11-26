from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodes = {}
        no_parents = set()
        for ind, word in enumerate(words):
            for ind_letter, letter in enumerate(word):
                if ind == 0:
                    nodes[letter] = [set(), set()] # parents, children
                    no_parents.add(letter)
                else:
                    previous = words[ind-1]
                    if word == previous[:len(word)]:
                        return ""
                    if len(previous) <= ind_letter:
                        if letter not in nodes: 
                            nodes[letter] = [set(), set()]
                            no_parents.add(letter)
                    else:
                        parent = previous[ind_letter]
                        if letter != parent:
                            # check for node
                            if letter in nodes:
                                nodes[letter][0].add(parent)
                                if letter in no_parents:
                                    no_parents.remove(letter)
                            else:
                                nodes[letter] = [set(parent), set()]
                            nodes[parent][1].add(letter)
        
        # topological sort
        order = []
        while len(no_parents)>0:
            letter = no_parents.pop()
            order.append(letter)
            for child in nodes[letter][1]:
                nodes[child][0].remove(letter)
                if len(nodes[child][0]) == 0:
                    no_parents.add(child)

        if len(order) == len(nodes):
            return "".join(order)
        else:
            return ""




solution = Solution()

words = ["wrtkj","wrt"]
assert solution.foreignDictionary(words) == ""

words = ["hrn","hrf","er","enn","rfnn"]
assert solution.foreignDictionary(words) == "hernf"

words = ["z","o"]
assert solution.foreignDictionary(words) == "zo"

words = ["z","o", "z"]
assert solution.foreignDictionary(words) == ""

