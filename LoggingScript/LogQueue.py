"""
Script to manage when logging a queue for misc. things...
"""

import collections


# class to store history of things...
class Queue:
    def __init__(self, max_length):
        self.que = collections.deque([0]*max_length, max_length)

    def add_to(self, data):
        self.que.pop()
        self.que.appendleft(data)


def queue_ex():
    q_test = Queue(5)

    for q in range(20):
        q_test.add_to(q)

    print(q_test.que)
    print(q_test.que[0])
