# https://www.acmicpc.net/problem/10773

################################################################
################### 스택 만들어서 푸는 방법 ######################
################################################################

# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     head = None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def pop(self):
#         self.head = self.head.next

#     def sum(self):
#         cur_node = self.head
#         sum = 0
#         while cur_node is not None:
#             sum += cur_node.data
#             cur_node = cur_node.next

#         print(sum)

# n = int(sys.stdin.readline())
# stack = Stack()

# for i in range(n):
#     money = int(sys.stdin.readline())

#     if money == 0:
#         stack.pop()
#     else:
#         stack.push(money)

# stack.sum()


################################################################
################### 배열 만들어서 푸는 방법 ######################
################################################################

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    money = int(sys.stdin.readline())

    if money == 0:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))
