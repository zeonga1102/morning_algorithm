# https://www.acmicpc.net/problem/10828

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    head = None
    count = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.head is None:
            print(-1)
        else:
            print(self.head.data)
            self.head = self.head.next
            self.count -= 1

    def size(self):        
        print(self.count)

    def empty(self):
        if self.head is None:
            print(1)
        else:
            print(0)

    def top(self):
        if self.head is None:
            print(-1)
        else:
            print(self.head.data)


n = int(sys.stdin.readline())
stack = Stack()

for i in range(n):

    input_list = sys.stdin.readline().split()

    cmd = input_list[0]

    if cmd == 'push':
        stack.push(int(input_list[1]))
    elif cmd =='pop':
        stack.pop()
    elif cmd == 'size':
        stack.size()
    elif cmd == 'empty':
        stack.empty()
    elif cmd == 'top':
        stack.top()


# n = int(sys.stdin.readline())

# stack = []

# for i in range(n):
#     cmd = sys.stdin.readline().split()

#     if cmd[0] == 'push':
#         stack.append(cmd[1])
#     elif cmd[0] == 'pop':
#         if len(stack) < 1:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif cmd[0] == 'size':
#         print(len(stack))
#     elif cmd[0] == 'empty':
#         if len(stack) < 1:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == 'top':
#         if len(stack) < 1:
#             print(-1)
#         else:
#             print(stack[-1])