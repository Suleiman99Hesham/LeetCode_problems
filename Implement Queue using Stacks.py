from collections import deque

class MyQueue:

    def __init__(self):
        self.queue=deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        try:
            return self.queue.popleft()
        except:
            return

    def peek(self) -> int:
        try:
            return self.queue[0]
        except:
            return

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.queue)
obj.push(1)
print(obj.queue)
obj.push(2)
print(obj.queue)
param_2 = obj.peek()
print(obj.queue)
# print(param_2)
param_3 = obj.pop()
print(obj.queue)
# print(param_3)
param_4 = obj.empty()
# print(obj.queue)
print(param_4)