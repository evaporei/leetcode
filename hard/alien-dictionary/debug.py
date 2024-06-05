from typing import List
from collections import defaultdict

class Solution:
    def alienDictionary(self, words: List[str]) -> str:
        edges = []
        for i in range(len(words) - 1):
            offset = 0
            while offset < len(words[i]) or offset < len(words[i+1]):
                if words[i][offset] != words[i+1][offset]:
                    edges.append((words[i][offset], words[i+1][offset]))
                    break
                else:
                    offset += 1
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        start = words[0][0]
        curr = start
        res = start
        while nodes := graph[curr]:
            res += nodes[0]
            curr = nodes[0]
        return res

s = Solution()
assert s.alienDictionary(['z', 'o']) == 'zo'
assert s.alienDictionary(["hrn","hrf","er","enn","rfnn"]) == 'hernf'
assert s.alienDictionary(['wrt', 'wrf', 'er', 'ett', 'rftt']) == 'wertf'
