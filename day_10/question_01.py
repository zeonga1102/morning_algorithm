# https://www.acmicpc.net/problem/4949

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

open_p_list = ['(', '{', '[']
close_p_list = [')', '}', ']']

while True:
    str = sys.stdin.readline()

    if str == '.\n':
        break

    stack = Stack()

    for i in str:
        if i in open_p_list:
            stack.push(i)
        elif i in close_p_list:
            if stack.peek() == open_p_list[close_p_list.index(i)]:
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack.peek() is not None:
            print('no')
        else:
            print('yes')
