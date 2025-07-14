from collections import deque

class WaitingQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0