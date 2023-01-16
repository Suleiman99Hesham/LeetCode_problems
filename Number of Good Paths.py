# import collections
# class Solution:
#     def numberOfGoodPaths(self, vals, edges) -> int:
#         if len(vals) == 1:
#             return 1
#         graph = collections.defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#         def is_good_path(previous, current, next, starting_value):
#             if vals[current] > starting_value:
#                 return False
#             if current == next:
#                 return True
#             childs = set(graph[current])
#             if next in childs:
#                 return True
#             if previous is not None:
#                 childs.remove(previous)
#             for child in childs:
#                 if is_good_path(current, child, next, starting_value): return True
#             return False

#         pairs = []
#         for start in range(0, len(vals)-1):
#             for end in range(start+1, len(vals)):
#                 if vals[start] == vals[end]:
#                     pairs.append((start,end))
#         good_paths = len(vals)
#         for pair in pairs:
#             if is_good_path(None, pair[0], pair[1], vals[pair[0]]):
#                 good_paths += 1
#         return good_paths

class Solution:
    def numberOfGoodPaths(self, vals, edges) -> int:

        def get_root(i):
            if i == par[i]: return i
            par[i] = get_root(par[i])
            return par[i]

        def connect(i, j):
            i,j = get_root(i), get_root(j)
           
            if i != j:
                if sz[i] < sz[j]: i, j = j, i
                par[j] = i
                sz[i] += sz[j]
                
                if cur[i] == cur[j]:
                    r = cnt[i] * cnt[j]
                    cnt[i] += cnt[j]
                    return r
                
                elif cur[i] < cur[j]:
                    cur[i],cnt[i] = cur[j],cnt[j]
            return 0
                    
        n = ans =len(vals)
        sz, cur,cnt, par  = [1]*n, vals,[1] *n, list(range(n))
        
        for a, b in sorted(edges, key=lambda p: max(vals[p[0]], vals[p[1]])):
            ans += connect(a, b)
            
        return ans

obj = Solution()
print(obj.numberOfGoodPaths([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]]))
print(obj.numberOfGoodPaths([2,4,1,2,2,5,3,4,4], [[0,1],[2,1],[0,3],[4,1],[4,5],[3,6],[7,5],[2,8]]))

