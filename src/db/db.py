import sqlite3
from src.data_structures.patient import Patient

DB_NAME = "hospital-system.db"


def init_db():
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                illness TEXT NOT NULL,
                emergency_level INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visits (
                patient_id INTEGER,
                visit_date TEXT,
                notes TEXT,
                FOREIGN KEY (patient_id) REFERENCES patients(id)
            )
        ''')
        conn.commit()
    finally:
        conn.close()


def insert_patient(patient):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (id, name, age, illness, emergency_level) VALUES (?, ?, ?, ?, ?)",
                       (patient.id, patient.name, patient.age, patient.illness, patient.emergency_level))
        conn.commit()
    finally:
        conn.close()


def update_patient(patient):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE patients SET name=?, age=?, illness=?, emergency_level=? WHERE id=?",
                       (patient.name, patient.age, patient.illness, patient.emergency_level, patient.id))
        conn.commit()
    finally:
        conn.close()


def delete_patient(patient_id):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
        conn.commit()
    finally:
        conn.close()


def get_patient_by_id(patient_id):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
        row = cursor.fetchone()
        if row:
            return Patient(*row)
        return None
    finally:
        conn.close()


def insert_visit(patient_id, visit_date, notes):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visits (patient_id, visit_date, notes) VALUES (?, ?, ?)",
                       (patient_id, visit_date, notes))
        conn.commit()
    finally:
        conn.close()


def get_visits_by_patient_id(patient_id):
    conn = sqlite3.connect(DB_NAME, timeout=5)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT visit_date, notes FROM visits WHERE patient_id=? ORDER BY visit_date DESC", (patient_id,))
        return cursor.fetchall()
    finally:
        conn.close()