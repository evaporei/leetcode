class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, node: int) -> int:
        res = node
        while res != self.parents[res]:
            self.parents[res] = self.parents[self.parents[res]]
            res = self.parents[res]
        return res
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for n1 in range(len(isConnected)):
            for n2 in range(len(isConnected)):
                if isConnected[n1][n2]:
                    uf.union(n1, n2)
        count = len(set((uf.find(i) for i in range(len(isConnected)))))
        return count
