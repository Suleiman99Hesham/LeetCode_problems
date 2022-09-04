# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.min = 0
        self.max = 0


    def verticalTraversal(self, root ):
        dic = {0 : [(0, root.val)]}
        
        def check_node(node, row, col):
            if col < self.min:
                self.min = col
            
            if col > self.max:
                self.max = col
            
            if col in dic:
                temp = dic[col]
                temp.append((row, node.val))
                dic[col] = temp
            else:
                dic[col] = [(row, node.val)]
            
            check_node(node=node.left, row=row+1, col=col-1) if node.left else None
            check_node(node=node.right, row=row+1, col=col+1) if node.right else None

        check_node(node=root.left, row=1, col=-1) if root.left else None
        check_node(node=root.right, row=1, col=1) if root.right else None

        return [[j[1] for j in sorted(dic[i], key=lambda x: (x[0], x[1])) ] for i in range(self.min, self.max+1)]