class LinkedListNode:
    def __init__(self, patient):
        self.patient = patient
        self.next = None


class HospitalLinkedList:
    def __init__(self):
        self.head = None

    def append(self, patient):
        new_node = LinkedListNode(patient)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, patient_id):
        current = self.head
        while current:
            if current.patient.id == patient_id:
                return current.patient
            current = current.next
        return None

    def delete(self, patient_id):
        current = self.head
        prev = None
        while current:
            if current.patient.id == patient_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def update(self, patient):
        current = self.head
        while current:
            if current.patient.id == patient.id:
                current.patient = patient
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.patient)
            current = current.next
        return result
