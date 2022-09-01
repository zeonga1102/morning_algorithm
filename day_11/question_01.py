# https://www.acmicpc.net/problem/18258

import sys
from collections import deque


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Queue:
#     head = None
#     tail = None
#     count = 0

#     def push(self, data):
#         self.count += 1

#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#             return

#         self.tail.next = new_node
#         self.tail = new_node

#     def pop(self):
#         if self.head == None:
#             print(-1)
#             return

#         self.count -= 1
        
#         print(self.head.data)
#         self.head = self.head.next

#     def size(self):
#         print(self.count)

#     def empty(self):
#         print(1) if self.head == None else print(0)

#     def front(self):
#         if self.head == None:
#             print(-1)
#             return

#         print(self.head.data)

#     def back(self):
#         if self.head == None:
#             print(-1)
#             return

#         print(self.tail.data)


# n = int(sys.stdin.readline())
# queue = Queue()

# for i in range(n):
#     input_list = sys.stdin.readline().split()

#     cmd = input_list[0]

#     if cmd == 'push':
#         queue.push(int(input_list[1]))
#     elif cmd =='pop':
#         queue.pop()
#     elif cmd =='pop':
#     elif cmd =='pop':
#     elif cmd =='pop':
#     elif cmd == 'size':
#         queue.size()
#     elif cmd == 'size':
#     elif cmd == 'size':
#     elif cmd == 'size':
#     elif cmd == 'empty':
#         queue.empty()
#     elif cmd == 'front':
#         queue.front()
#     elif cmd == 'back':
#         queue.back()

n = int(sys.stdin.readline())

dq = deque([])
for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(dq) < 1:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if len(dq) < 1:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(dq) < 1:
            print(-1)
        else:
            print(dq[0])
    elif cmd[0] == 'back':
        if len(dq) < 1:
            print(-1)
        else:
            print(dq[-1])