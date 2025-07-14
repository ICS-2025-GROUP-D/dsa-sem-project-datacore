import tkinter as tk
from tkinter import messagebox
from src.data_structures.patient import Patient
from src.db.db import init_db, insert_patient, update_patient, delete_patient, get_patient_by_id, insert_visit, get_visits_by_patient_id
from src.data_structures.bst import PatientBST
from src.data_structures.hash_table import PatientHashTable
from src.data_structures.queue import WaitingQueue
from src.data_structures.stack import Undo
from src.data_structures.heap import EmergencyHeap
from src.data_structures.hospital_linkedlist import HospitalLinkedList
from datetime import datetime

init_db()

bst = PatientBST()
hash_table = PatientHashTable()
queue = WaitingQueue()
undo_stack = Undo()
heap = EmergencyHeap()
linked_list = HospitalLinkedList()

def add_patient(patient):
    insert_patient(patient)
    bst.insert(patient)
    hash_table.insert(patient)
    queue.enqueue(patient)
    heap.add_patient(patient)
    linked_list.append(patient)
    undo_stack.push(('delete', patient))

def update_patient_record(patient):
    old = get_patient_by_id(patient.id)
    if old:
        update_patient(patient)
        bst.delete(old.id)
        bst.insert(patient)
        hash_table.insert(patient)
        undo_stack.push(('update', old))

def delete_patient_record(patient_id):
    patient = get_patient_by_id(patient_id)
    if patient:
        delete_patient(patient_id)
        bst.delete(patient_id)
        hash_table.delete(patient_id)
        undo_stack.push(('add', patient))

def view_visits(patient_id):
    return get_visits_by_patient_id(patient_id)

def treat_next_patient():
    patient = heap.treat_next()
    if patient:
        insert_visit(patient.id, datetime.now().isoformat(), f"Treated for {patient.illness}")
        print(f"Treated: {patient}")
    else:
        print("No patients to treat.")

def undo_last():
    if undo_stack.is_empty():
        messagebox.showinfo("Undo", "Nothing to undo.")
        return

    action, patient = undo_stack.pop()
    if action == 'delete':
        delete_patient(patient.id)
        bst.delete(patient.id)
        hash_table.delete(patient.id)
    elif action == 'add':
        insert_patient(patient)
        bst.insert(patient)
        hash_table.insert(patient)
    elif action == 'update':
        update_patient(patient)
        bst.delete(patient.id)
        bst.insert(patient)
        hash_table.insert(patient)

def add_visit_entry(patient_id, notes="Routine check"):
    insert_visit(patient_id, datetime.now().isoformat(), notes)

def setup_gui():
    root = tk.Tk()
    root.title("Hospital Management System")
    root.geometry("500x650")

    id_entry = tk.Entry(root)
    name_entry = tk.Entry(root)
    age_entry = tk.Entry(root)
    illness_entry = tk.Entry(root)
    emergency_entry = tk.Entry(root)
    notes_entry = tk.Entry(root)

    entries = [id_entry, name_entry, age_entry, illness_entry, emergency_entry, notes_entry]

    for i, (label_text, entry) in enumerate([
        ("Patient ID", id_entry),
        ("Name", name_entry),
        ("Age", age_entry),
        ("Illness", illness_entry),
        ("Emergency Level (1-3)", emergency_entry),
        ("Visit Notes", notes_entry)
    ]):
        tk.Label(root, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entry.grid(row=i, column=1, padx=5, pady=5)

    def handle_add():
        try:
            age = int(age_entry.get())
            level = int(emergency_entry.get())
            if not (1 <= level <= 3):
                raise ValueError("Emergency level must be between 1 and 3.")
            patient = Patient(int(id_entry.get()), name_entry.get(), age, illness_entry.get(), level)
            add_patient(patient)
            messagebox.showinfo("Success", "Patient added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_update():
        try:
            age = int(age_entry.get())
            level = int(emergency_entry.get())
            patient = Patient(int(id_entry.get()), name_entry.get(), age, illness_entry.get(), level)
            update_patient_record(patient)
            messagebox.showinfo("Success", "Patient updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_delete():
        try:
            delete_patient_record(int(id_entry.get()))
            messagebox.showinfo("Success", "Patient deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_view_visits():
        try:
            visits = view_visits(int(id_entry.get()))
            if visits:
                result = "\n".join([f"{v[0]} - {v[1]}" for v in visits])
                messagebox.showinfo("Visit History", result)
            else:
                messagebox.showinfo("Visit History", "No visits found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_treat():
        treat_next_patient()
        messagebox.showinfo("Treated", "Next patient has been treated (if available)")

    def handle_undo():
        undo_last()

    def handle_add_visit():
        try:
            pid = int(id_entry.get())
            notes = notes_entry.get() or "Routine check"
            add_visit_entry(pid, notes)
            messagebox.showinfo("Success", "Visit logged successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Add", command=handle_add).grid(row=6, column=0)
    tk.Button(root, text="Update", command=handle_update).grid(row=6, column=1)
    tk.Button(root, text="Delete", command=handle_delete).grid(row=7, column=0)
    tk.Button(root, text="View Visits", command=handle_view_visits).grid(row=7, column=1)
    tk.Button(root, text="Treat Emergency", command=handle_treat).grid(row=8, column=0)
    tk.Button(root, text="Undo", command=handle_undo).grid(row=8, column=1)
    tk.Button(root, text="Add Visit", command=handle_add_visit).grid(row=9, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    setup_gui()