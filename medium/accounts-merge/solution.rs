struct UnionFind {
    parents: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            parents: (0..n).into_iter().collect(),
            rank: vec![1; n],
        }
    }

    fn find(&mut self, node: usize) -> usize {
        let mut res = node;

        while res != self.parents[res] {
            self.parents[res] = self.parents[self.parents[res]];
            res = self.parents[res]
        }

        res
    }

    fn union_(&mut self, n1: usize, n2: usize) -> bool {
        let (p1, p2) = (self.find(n1), self.find(n2));
        if p1 == p2 {
            return false;
        }

        if self.rank[p1] > self.rank[p2] {
            self.parents[p2] = p1;
            self.rank[p1] += self.rank[p2];
        } else {
            self.parents[p1] = p2;
            self.rank[p2] += self.rank[p1];
        }

        true
    }
}

use std::collections::HashMap;

impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut email_to_acc: HashMap<String, usize> = HashMap::new();
        let mut uf = UnionFind::new(accounts.len());

        for (i, account) in accounts.iter().enumerate() {
            for email in account.iter().skip(1) {
                if email_to_acc.contains_key(email) {
                    uf.union_(i, email_to_acc[email]);
                } else {
                    email_to_acc.insert(email.to_owned(), i);
                }
            }
        }

        let mut email_groups = HashMap::new();
        for (email, i) in email_to_acc {
            let root = uf.find(i);
            email_groups.entry(root)
                .and_modify(|v: &mut Vec<_>| v.push(email.clone()))
                .or_insert(vec![email]);
        }

        let mut res = Vec::with_capacity(accounts.len());
        for (i, mut emails) in email_groups {
            let name = accounts[i][0].clone();
            let mut account = vec![name];
            emails.sort();
            account.append(&mut emails);
            res.push(account);
        }

        res
    }
}
