# https://leetcode.com/problems/accounts-merge/description/

# Time: O(N * α(N)) where N is the total number of emails, and α is the inverse Ackermann function from Union-Find operations.
# Space: O(N) for storing parents, email-name mappings, and final groups.




from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        root_to_emails = defaultdict(set)
        for email in email_to_name:
            root = uf.find(email)
            root_to_emails[root].add(email)

        result = []
        for root, emails in root_to_emails.items():
            result.append([email_to_name[root]] + sorted(emails))
        
        return result
        