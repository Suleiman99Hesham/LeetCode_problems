class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode):
        sums = []
        counts = []
        level = 0
        def collect_values(node, level):
            if level >= len(sums):
                sums.append(0)
            if level >= len(counts):
                counts.append(0)
            sums[level] += node.val
            counts[level]  +=1 
            collect_values(node.left, level+1) if node.left else None
            collect_values(node.right, level+1) if node.right else None
            return
        collect_values(root, level) if root else  None

        for idx, value in enumerate(sums):
            sums[idx] = (value/counts[idx])

        return sums

l2 = TreeNode(15)
r2 = TreeNode(7)
l1 = TreeNode(9 , l2, r2)
r1 = TreeNode(20)
root = TreeNode(3, l1, r1)

print(Solution().averageOfLevels(root))