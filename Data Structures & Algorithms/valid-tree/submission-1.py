class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(list)
        for e in edges:
            edgeMap[e[0]].append(e[1])
            edgeMap[e[1]].append(e[0])

        visited = set()
        # returns True if node is a valid tree root
        def dfs(parent: int, curr: int) -> bool:
            if curr in visited:
                return False
            visited.add(curr)

            for n in edgeMap[curr]:
                if n != parent and not dfs(curr, n):
                    return False
                    
            return True
        
        # treat node 0 as the root
        # in a tree with undirected edges, any node can be the root node
        # now we traverse this tree and make sure theres no cycle
        if not dfs(-1, 0):
            return False
        
        # now we check if all the nodes have been visited
        return len(visited) == n