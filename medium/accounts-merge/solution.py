class UnionFind:
    parents: List[int]
    rank: List[int]

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
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_acc = {}
        uf = UnionFind(len(accounts))

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        
        email_groups = defaultdict(list)
        for email, i in email_to_acc.items():
            root = uf.find(i)
            email_groups[root].append(email)
        
        res = []
        for i, emails in email_groups.items():
            name = accounts[i][0]
            emails.sort()
            res.append([name] + emails)

        return res
