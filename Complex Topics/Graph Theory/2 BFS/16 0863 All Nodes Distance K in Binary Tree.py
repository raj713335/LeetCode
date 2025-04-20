# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        # Step 1: Convert binary tree to graph (undirected)
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: BFS from target to find all nodes at distance k
        visited = set()
        queue = deque([(target.val, 0)])
        res = []

        while queue:
            node, dist = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if dist == k:
                res.append(node)
            elif dist < k:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

        return res
        
