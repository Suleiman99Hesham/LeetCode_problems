# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.string = ''
    def tree2str(self, root):
        def get_string(node):
            self.string = f'({node.val}'
            if node.left:
                self.string += get_string(node.left) 
            elif not node.left and node.right:
                self.string += '()'
            self.string += get_string(node.right) if node.right else ''
            self.string += ')'
            return self.string
        self.string = f'{root.val}'
        if root.left:
            self.string += get_string(root.left) 
        elif not root.left and root.right:
            self.string += '()'
        self.string += get_string(root.right) if root.right else ''
        return self.string