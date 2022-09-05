"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []        
        q = deque([root] if root else [])
        while q:
            result.append([])
            for _ in range(len(q)):
                node = q.popleft()
                result[-1].append(node.val)
                q.extend(node.children)
            
        return result