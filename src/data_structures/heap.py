import heapq

class EmergencyHeap:
    def __init__(self):
        self.heap = []

    def add_patient(self, patient):
        heapq.heappush(self.heap, (patient.emergency_level, patient))

    def treat_next(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def is_empty(self):
        return len(self.heap) == 0
