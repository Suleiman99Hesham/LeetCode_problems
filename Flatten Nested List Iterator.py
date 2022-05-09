# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def __init__(self, value):
#         self.value = value

#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#         return True if self.value == int else False

#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#         return self.value if self.value == int else None

#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """
#         return self.value if self.value == list else None

import collections

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


class NestedIterator:
    def __init__(self, nestedList):
        self.flatten_array = list(self.flatten(nestedList))
        self.len_flatten_array = len(self.flatten_array)
        self.counter = 0

    def flatten(self, lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in self.flatten(item):
                    yield x
            else:        
                yield item

    def next(self) -> int:
        if self.counter < self.len_flatten_array:
            self.counter += 1
            return self.flatten_array[self.counter-1]
        return None

    def hasNext(self) -> bool:
        return True if self.counter < self.len_flatten_array else False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
