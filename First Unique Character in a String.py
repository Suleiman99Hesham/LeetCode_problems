class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        unique_chars=[]
        for i,val in enumerate(s):
            if val in freq:
                if freq[val] == -1:
                    continue
                freq[val] = -1
                unique_chars.remove(val)
            else:
                freq[val] = i
                unique_chars.append(val)
        if unique_chars:
            return freq[unique_chars[0]]
        else: return -1

obj = Solution()
print(obj.firstUniqChar("aabb"))