from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


class Solution:
    visited = set()
    from_to = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        else:
            self.visited.add(node)
            n = Node(node.val)
            self.from_to[node] = n
            for e in node.neighbors:
                if e in self.visited:
                    n.neighbors.append(self.from_to[e])
                else:
                    n.neighbors.append(self.cloneGraph(e))
        return n
