# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_good(self, node: TreeNode, greatest=0):
        greatest = greatest if greatest >= node.val else node.val
        good = 1 if greatest == node.val else 0
        good += self.check_good(node.left, greatest) if node.left else 0
        good += self.check_good(node.right, greatest) if node.right else 0
        return good
        
    def goodNodes(self, root: TreeNode) -> int:
        greatest = root.val
        good = 1
        good += self.check_good(root.left, greatest) if root.left else 0
        good += self.check_good(root.right, greatest) if root.right else 0
        return good