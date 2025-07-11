import tkinter as tk
from tkinter import messagebox
from src.db.db import (
    insert_patient, delete_patient_from_db, update_patient_in_db,
    get_patient_from_db, init_db, insert_visit, get_visits,
    insert_emergency, get_next_emergency
)
from src.data_structures.bst import PatientBST
from src.data_structures.hash_table import PatientHashTable, Patient
from src.data_structures.queue import WaitingQueue
from src.data_structures.stack import Undo
from src.data_structures.heap import EmergencyHeap
from src.data_structures.hospital_linkedlist import HospitalLinkedList

bst = PatientBST()
hash_table = PatientHashTable()
queue = WaitingQueue()
undo = Undo()
heap = EmergencyHeap()
linked_list = HospitalLinkedList()

init_db()

# GUI logic
def add_patient():
    try:
        pid = int(entry_id.get())
        name = entry_name.get()
        age = int(entry_age.get())
        illness = entry_illness.get()

        patient = {'id': pid, 'name': name, 'age': age, 'illness': illness}
        bst.insert(patient)
        insert_patient(pid, name, age, illness)
        hash_table.insert(Patient(pid, name, age, illness))
        queue.enqueue(Patient(pid, name, age, illness))
        linked_list.add_visit(pid, f"Visit for {illness}")
        insert_visit(pid, f"Visit for {illness}")
        undo.push(('add', patient))

        messagebox.showinfo("Success", f"Patient {name} added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_patient():
    try:
        pid = int(entry_id.get())
        patient = bst.search(pid)
        if patient:
            messagebox.showinfo("Found", f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
        else:
            row = get_patient_from_db(pid)
            if row:
                messagebox.showinfo("Found in DB", f"Name: {row[1]}, Age: {row[2]}, Illness: {row[3]}")
            else:
                messagebox.showwarning("Not Found", "No patient with that ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_patient():
    try:
        pid = int(entry_id.get())
        patient = bst.search(pid)
        if patient:
            bst.delete(pid)
            delete_patient_from_db(pid)
            undo.push(('delete', patient))
            messagebox.showinfo("Deleted", f"Patient with ID {pid} deleted.")
        else:
            messagebox.showwarning("Not Found", "Patient not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_patient():
    try:
        pid = int(entry_id.get())
        name = entry_name.get()
        age = int(entry_age.get())
        illness = entry_illness.get()

        existing = bst.search(pid)
        if existing:
            bst.delete(pid)
            patient = {'id': pid, 'name': name, 'age': age, 'illness': illness}
            bst.insert(patient)
            update_patient_in_db(pid, name, age, illness)
            hash_table.insert(Patient(pid, name, age, illness))
            linked_list.add_visit(pid, f"Update visit - {illness}")
            insert_visit(pid, f"Update visit - {illness}")
            messagebox.showinfo("Updated", f"Patient ID {pid} updated.")
        else:
            messagebox.showwarning("Not Found", "Patient not found to update.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def undo_last_action():
    try:
        action, patient = undo.pop()
        if action == 'add':
            bst.delete(patient['id'])
            delete_patient_from_db(patient['id'])
        elif action == 'delete':
            bst.insert(patient)
            insert_patient(patient['id'], patient['name'], patient['age'], patient['illness'])
        messagebox.showinfo("Undo", f"Undid last action: {action} patient {patient['name']}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def treat_next_emergency():
    try:
        emergency = get_next_emergency()
        if emergency:
            messagebox.showinfo("Treated", f"Emergency patient treated: {emergency[1]} (ID: {emergency[0]})")
        else:
            messagebox.showinfo("No Emergency", "No emergency patients to treat.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_visit_history():
    try:
        pid = int(entry_id.get())
        history = get_visits(pid)
        if history:
            messagebox.showinfo("Visit History", "\n".join([v[0] for v in history]))
        else:
            messagebox.showinfo("Visit History", "No visits found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Hospital Management System")

tk.Label(root, text="Patient ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Age").grid(row=2, column=0)
tk.Label(root, text="Illness").grid(row=3, column=0)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_illness = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_age.grid(row=2, column=1)
entry_illness.grid(row=3, column=1)

tk.Button(root, text="Add", command=add_patient).grid(row=4, column=0)
tk.Button(root, text="Search", command=search_patient).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_patient).grid(row=5, column=0)
tk.Button(root, text="Update", command=update_patient).grid(row=5, column=1)
tk.Button(root, text="Undo Last", command=undo_last_action).grid(row=6, column=0)
tk.Button(root, text="Treat Emergency", command=treat_next_emergency).grid(row=6, column=1)
tk.Button(root, text="Visit History", command=view_visit_history).grid(row=7, column=0, columnspan=2)

root.mainloop()
