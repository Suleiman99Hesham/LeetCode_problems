class Solution:
    def isValid(self, s: str) -> bool:
        history=[]
        if len(s) == 1:
            return False
        for item in s:
            if item not in '[](){}':
                return False
            if item in ['[','(','{']:
                history.append(item)
            elif (item == ']' or item == ')' or item == '}') and len(history) == 0:
                return False
            elif item == ']' and history[-1] == '[':
                history.pop()
            elif item == ')' and history[-1] == '(':
                history.pop()
            elif item == '}' and history[-1] == '{':
                history.pop()
            else:
                return False
        if len(history) == 0:
            return True
        else:
            return False

# class Solution:
#     def isValid(self, s: str) -> bool:
#         lis=[]
#         for i in s:
#             lis.append(i)
#             if len(lis)>1:
#                 if(ord(lis[-1])-ord(lis[-2])==1 or ord(lis[-1])-ord(lis[-2])==2):
#                     lis.pop()
#                     lis.pop()
#         if len(lis)==0:
#             return True
#         else:
#             return False

obj=Solution()
print(obj.isValid("{[(){}{|]}"))