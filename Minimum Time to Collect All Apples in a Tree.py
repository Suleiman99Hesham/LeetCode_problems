import collections 
class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            ans = 0
            for child in graph[node]:
                if child == parent:
                    continue
                ans += dfs(child, node)
            if (ans > 0 or hasApple[node]) and node != 0:
                ans += 2
            return ans
        return  dfs(0, -1)

# class Solution:
#     def minTime(self, n: int, edges, hasApple) -> int:
#         has_apples_indexes = []
#         for idx, apple in enumerate(hasApple):
#             if apple:
#                 has_apples_indexes.append(idx)
#         if len(has_apples_indexes) == 0:
#             return 0

#         apples_form_0 = [[0] for _ in range(len(has_apples_indexes))]
#         for idx, node_value in enumerate(has_apples_indexes):
#             if node_value == 0:
#                 continue
#             apples_form_0[idx].append(node_value)
#             search_for = node_value
#             while search_for != 0:
#                 for edge in edges:
#                     edge = sorted(edge)
#                     if edge[1] == search_for:
#                         search_for = edge[0]
#                         if edge[0] != 0:
#                             apples_form_0[idx].insert(1,edge[0])
#                         break
#         for first_list in apples_form_0:
#             for sec_list in apples_form_0:
#                 if first_list != sec_list and set(sec_list).issubset(set(first_list)):
#                     apples_form_0.remove(sec_list)
                     
#         old_path = []
#         min_count = 0
#         for path in apples_form_0 :
#             intersection = list(set(path) & set(old_path))
#             if len(intersection) < 2:
#                 min_count += len(old_path) - 1 if len(old_path) > 0 else 0
#                 min_count += len(path) - 1
#             else:
#                 min_count += len(old_path) - old_path.index(intersection[-1]) - 1
#                 min_count += len(path) - path.index(intersection[-1]) - 1
#             old_path = path
#         min_count += len(old_path) - 1
#         return min_count


# class Solution:
#     def minTime(self, n: int, edges, hasApple) -> int:
#         if hasApple.count(True) == 0:
#             return 0
#         edges_vertices = {}
#         for i in range(n):
#             for edge in edges:
#                 x = -1
#                 if edge[0] == i:
#                     x = edge[1]
#                 elif edge[1] == i:
#                     x =edge[0]
#                 if x != -1:
#                     if i in edges_vertices.keys():
#                         edges_vertices[i].append(x)
#                     else:
#                         edges_vertices[i] = [x]

#         def check_node(node_value, previous_node=None):
#             if node_value == n:
#                 return 0
#             counted = 0
#             currunt = False
#             if hasApple[node_value] and node_value != 0:
#                 counted = 1
#                 currunt = True
#             node_vertices = edges_vertices[node_value]
#             node_vertices.remove(previous_node) if previous_node != -1 else None
#             for v in node_vertices:
#                 counted += check_node(v, node_value)
#             return counted + 1 if not currunt and counted > 0 and node_value != 0 else counted
            
#         return check_node(0, -1) * 2
                    

obj = Solution()
print(obj.minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))
# print(obj.minTime(4,[[0,1],[1,2],[0,3]],[True,True,True,True]))
# print(obj.minTime(4,[[0,1],[0,2],[1,3],[0,4]],[False,True,True,True, False]))
# print(obj.minTime(4,[[0,2],[0,3],[1,2]],[False,True,False, False]))
        