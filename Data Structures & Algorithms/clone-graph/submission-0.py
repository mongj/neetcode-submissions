"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited = set()
        oldGraph = {}

        def dfs(node: Optional['Node']) -> None:
            if not node:
                return
            if node in visited:
                return
            visited.add(node)

            oldGraph[node.val] = (Node(val=node.val), [])
            for neighbor in node.neighbors:
                oldGraph[node.val][1].append(neighbor.val)
                dfs(neighbor)

        dfs(node)
        
        # link up the neighbors
        for node, neighbors in oldGraph.values():
            for neighbor in neighbors:
                node.neighbors.append(oldGraph[neighbor][0])

        return oldGraph[1][0]
