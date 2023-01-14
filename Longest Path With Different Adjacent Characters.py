import collections
class Solution:
    def longestPath(self, parent, s: str) -> int:
        if len(parent) == 1:
            return 1
        graph = collections.defaultdict(list)
        for i, v in enumerate(parent):
            graph[v].append(i)
        self.max_path_len = 0
        def search_path(node):
            childs_paths_values = []
            for child in graph[node]:
                s_node = s[node]
                s_child = s[child]
                if s_node != s_child:
                    childs_paths_values.append(search_path(child))
                else:
                    search_path(child)
            childs_paths_values =  sorted(childs_paths_values, reverse=True)
            if len(childs_paths_values) >= 2:
                node_value = childs_paths_values[0] + childs_paths_values[1] + 1
            else:
                node_value = max(childs_paths_values) + 1 if len(childs_paths_values) > 0 else 1
            if node_value > self.max_path_len:
                self.max_path_len = node_value
            return max(childs_paths_values) + 1 if len(childs_paths_values) > 0 else 1
        return max(search_path(0), self.max_path_len)

obj = Solution()
print(obj.longestPath([-1,0,0,1,1,2], "abacbe"))
print(obj.longestPath([-1,0,0,0], "aabc"))
print(obj.longestPath([-1,0,1], "aab"))