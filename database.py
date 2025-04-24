import sqlite3

#create the  database 
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

#creating a note table if it doesnt existts

cursor.execute('''
               CREATE TABLE IF NOT EXISTS notes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   content TEXT NOT NULL
               )
               ''')

def add_note(title,content):
    cursor.execute("INSERT INTO notes(title ,content) VALUES(?,?)",(title,content))
    conn.commit()
    
def get_all_note():
    cursor.execute("SELECT * FROM notes")
    return cursor.fetchall()

def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()

def update_note(note_id, new_title,new_content):
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
    conn.commit()

def close_connection():
    conn.close()
