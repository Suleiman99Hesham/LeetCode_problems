# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if (p.val != q.val):
            return False
        
        l = self.isSameTree(p.right, q.right)
        r = self.isSameTree(p.left, q.left)
        if l != False and r != False:
            return True
        return False

r2 = TreeNode(3)
l2 = TreeNode(2)
root2 = TreeNode(1, l2,r2)

r1 = TreeNode(3)
l1 = TreeNode(2)
root1 = TreeNode(1, l1,r1)

obj = Solution()
print(obj.isSameTree(root1, root2))