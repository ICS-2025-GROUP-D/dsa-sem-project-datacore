import sqlite3

def init_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            illness TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER,
            note TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS emergency (
            id INTEGER PRIMARY KEY,
            name TEXT,
            urgency INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_patient(pid, name, age, illness):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO patients VALUES (?, ?, ?, ?)', (pid, name, age, illness))
    conn.commit()
    conn.close()

def get_patient_from_db(pid):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('SELECT * FROM patients WHERE id = ?', (pid,))
    result = c.fetchone()
    conn.close()
    return result

def delete_patient_from_db(pid):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('DELETE FROM patients WHERE id = ?', (pid,))
    conn.commit()
    conn.close()

def update_patient_in_db(pid, name, age, illness):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('UPDATE patients SET name=?, age=?, illness=? WHERE id=?', (name, age, illness, pid))
    conn.commit()
    conn.close()

def insert_visit(pid, note):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('INSERT INTO visits (id, note) VALUES (?, ?)', (pid, note))
    conn.commit()
    conn.close()

def get_visits(pid):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('SELECT note FROM visits WHERE id = ?', (pid,))
    results = c.fetchall()
    conn.close()
    return results

def insert_emergency(pid, name, urgency):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO emergency VALUES (?, ?, ?)', (pid, name, urgency))
    conn.commit()
    conn.close()

def get_next_emergency():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('SELECT * FROM emergency ORDER BY urgency DESC LIMIT 1')
    result = c.fetchone()
    if result:
        c.execute('DELETE FROM emergency WHERE id = ?', (result[0],))
        conn.commit()
    conn.close()
    return result
