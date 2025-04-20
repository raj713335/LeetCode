# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/

from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # Step 1: Assign unique groups to ungrouped items
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1

        # Step 2: Build graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * new_group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # If in different groups, create group dependency
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        # Step 3: Topo sort function
        def topological_sort(graph, indegree, total):
            res = []
            q = deque([i for i in range(total) if indegree[i] == 0])
            while q:
                node = q.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return res if len(res) == total else []

        # Step 4: Topo sort items and groups
        item_order = topological_sort(item_graph, item_indegree, n)
        group_order = topological_sort(group_graph, group_indegree, new_group_id)

        if not item_order or not group_order:
            return []

        # Step 5: Group items based on their group
        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        # Step 6: Flatten final answer by group order
        res = []
        for grp in group_order:
            res.extend(grouped_items[grp])
        return res
        
