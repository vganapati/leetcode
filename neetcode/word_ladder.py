"""
https://neetcode.io/problems/word-ladder
"""

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create adjacency list of wordList
        wordList.append(beginWord)
        adj = defaultdict(list)
        for i, word_i in enumerate(wordList):
            for word_j in wordList[i+1:]:
                # check if the words can be transformed by 1 letter
                if sum([c0 != c1 for c0,c1 in zip(word_i,word_j)]) == 1:
                    adj[word_i].append(word_j)
                    adj[word_j].append(word_i)
        
        # start at beginWord and BFS with minHeap to get to endWord
        minHeap = [[1,beginWord]]
        visited = set()

        while minHeap:
            dist, word = heapq.heappop(minHeap)
            if word == endWord:
                return dist
            visited.add(word)
            for child in adj[word]:
                if child not in visited:
                    heapq.heappush(minHeap, [dist+1, child])
        
        return 0

solution = Solution()

beginWord = "cat"; endWord = "sag"; wordList = ["bat","bag","sag","dag","dot"]
assert solution.ladderLength(beginWord, endWord, wordList) == 4

beginWord = "cat"; endWord = "sag"; wordList = ["bat","bag","sat","dag","dot"]
assert solution.ladderLength(beginWord, endWord, wordList) == 0
