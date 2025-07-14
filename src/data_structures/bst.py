class PatientNode:
    def __init__(self, patient):
        self.patient = patient  # patient should be a dict with at least an 'id' field
        self.left = None
        self.right = None


class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, patient):
        def _insert(node, patient):
            if node is None:
                return PatientNode(patient)
            if patient["id"] < node.patient["id"]:
                node.left = _insert(node.left, patient)
            else:
                node.right = _insert(node.right, patient)
            return node
        self.root = _insert(self.root, patient)

    def delete(self, patient_id):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, patient_id):
            if node is None:
                return None

            if patient_id < node.patient["id"]:
                node.left = _delete(node.left, patient_id)
            elif patient_id > node.patient["id"]:
                node.right = _delete(node.right, patient_id)
            else:
                # Node with one or no children
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children
                min_node = _min_value_node(node.right)
                node.patient = min_node.patient
                node.right = _delete(node.right, min_node.patient["id"])

            return node

        self.root = _delete(self.root, patient_id)

    def search(self, patient_id):
        def _search(node, patient_id):
            if node is None:
                return None
            if patient_id == node.patient["id"]:
                return node.patient
            elif patient_id < node.patient["id"]:
                return _search(node.left, patient_id)
            else:
                return _search(node.right, patient_id)

        return _search(self.root, patient_id)

    def in_order(self):
        def _in_order(node):
            if node is None:
                return []
            return _in_order(node.left) + [node.patient] + _in_order(node.right)

        return _in_order(self.root)
