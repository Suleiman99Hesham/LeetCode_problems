import collections
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        container = {}

        def discover(node, parent):
            node_counts = {labels[node] : 1}
            for child_node in graph[node]:
                if child_node == parent: continue
                child_counts = container.get(child_node, None)
                if child_counts is None:
                    child_counts = discover(child_node, node)
                    container[child_node] = child_counts
                for label, count in child_counts.items():
                    node_counts[label] = node_counts.get(label, 0) + count
            return node_counts
        
        container[0] = discover(0, -1)
        return [container[i][labels[i]] for i in range(n)]

obj = Solution()
print(obj.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],'abaedcd'))
print(obj.countSubTrees(4, [[0,1],[1,2],[0,3]],'bbbb'))
print(obj.countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]],'aabab'))