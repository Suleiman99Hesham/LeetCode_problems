class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode):
        counts = {}
        def collect_values(node, level):
            if level in counts:
                counts[level][0] += node.val
                counts[level][1] += 1
            else:
                counts[level] = [node.val, 1]

            collect_values(node.left, level+1) if node.left else None
            collect_values(node.right, level+1) if node.right else None
            return
        collect_values(root, 0) if root else  None

        i=0
        result = []
        while counts:
            result.append(counts[i][0]/counts[i][1])
            del counts[i]
            i+=1
            

        return result