from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_map = {}

        def dfs(current_node):
            if current_node in cloned_map:
                return cloned_map[current_node]

            clone = Node(current_node.val)
            cloned_map[current_node] = clone

            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
