# https://www.acmicpc.net/problem/9012

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
        self.head = self.head.next

    def peek(self):
        if self.head == None:
            return None

        return self.head.data


n = int(sys.stdin.readline())

for i in range(n):
    stack = Stack()
    ps = sys.stdin.readline()
    for j in ps:
        if j == '(':
            stack.push('(')
        elif j == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack.peek() is not None:
            print('NO')
        else:
            print('YES')