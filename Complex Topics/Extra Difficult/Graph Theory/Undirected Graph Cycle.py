# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/

from collections import defaultdict

class Solution:
	def isCycle(self, V, edges):
		#Code here
		
		adjency_list = defaultdict(list)
		
		for u, v in edges:
		    adjency_list[u].append(v)
		    adjency_list[v].append(u)
		    
		visited = set()
		
		def dfs(node, adjency_list, visited, parent):
            visited.add(node)
            
            for next in adjency_list[node]:
                if next not in visited:
                    ans = dfs(next, adjency_list, visited, node)
                    if ans:
                        return True
                elif next in visited and next != parent:
                    return True
            return False
		
		for node in range(V):
		    if node not in visited:
		        ans = dfs(node, adjency_list, visited, -1)
		        if ans:
		            return True
		return False


#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
