# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode ) -> list:
        if not root: return []
        array = []
        stack = []
        while True:
            array.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                root = root.left
            elif stack:
                root = stack.pop()
            else:
                return array
n5=None
n4=TreeNode(3)
n3=TreeNode(2,n4,n5)
n2=None
root=TreeNode(1,n2,n3)

obj=Solution()
print(obj.preorderTraversal(root))




# class Solution:
#     def preorderTraversal(self, root: TreeNode ) -> list:
#         if not root:
#             return []
#         answer=[]
#         stack = []
#         while True:
#             answer.append(root.val)
#             if type(root.left) == TreeNode:
#                 if root.right:
#                     stack.append(root.right)
#                 root=root.left
#             else:
#                 if type(root.left) == int:
#                     answer.append(root.left)
#                 if type(root.right) == TreeNode:
#                     root=root.right
#                 else:
#                     if type(root.right) == int:
#                         answer.append(root.right)
#                     if len(stack) > 0:
#                         root = stack.pop()
#                     else: stack = None
#             if stack == None:
#                 break
#         return answer