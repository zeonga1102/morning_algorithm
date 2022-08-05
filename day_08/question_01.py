# https://www.acmicpc.net/problem/10828

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print(-1)
        else:
            print(self.head.data)
            self.head = self.head.next

    def size(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        
        print(count)

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