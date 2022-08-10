# https://www.acmicpc.net/problem/18258

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    head = None
    tail = None
    count = 0

    def push(self, data):
        self.count += 1

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.head == None:
            print(-1)
            return

        self.count -= 1
        
        print(self.head.data)
        self.head = self.head.next

    def size(self):
        print(self.count)

    def empty(self):
        print(1) if self.head == None else print(0)

    def front(self):
        if self.head == None:
            print(-1)
            return

        print(self.head.data)

    def back(self):
        if self.head == None:
            print(-1)
            return

        print(self.tail.data)


n = int(sys.stdin.readline())
queue = Queue()

for i in range(n):
    input_list = sys.stdin.readline().split()

    cmd = input_list[0]

    if cmd == 'push':
        queue.push(int(input_list[1]))
    elif cmd =='pop':
        queue.pop()
    elif cmd == 'size':
        queue.size()
    elif cmd == 'empty':
        queue.empty()
    elif cmd == 'front':
        queue.front()
    elif cmd == 'back':
        queue.back()