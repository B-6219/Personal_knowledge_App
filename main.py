import tkinter as tk
from tkinter import messagebox
from database import *  # Assuming the database code is saved in database.py

#Create the main window
root = tk.Tk()
root.title("Notes App")
root.geometry("600x400")  # Size of the window
root.config(bg="#2F2F2F")

#Label for the title field
title_label = tk.Label(root, text="Title", fg="white", bg="#2F2F2F", font=("Arial", 12))
title_label.pack(pady=10)

#Entry widget for entering the title
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

#Label for the content field
content_label = tk.Label(root, text="Content", fg="white", bg="#2F2F2F", font=("Arial", 12))
content_label.pack(pady=10)

#Text box for entering the content of the note
content_text = tk.Text(root, height=5, width=50)
content_text.pack(pady=5)

#Function to add a new note to the database
def add_note():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    
    if title == "" or content == "":
        messagebox.showerror("Input Error", "Please fill out both fields")
        return
    
    # Add the note to the database
    add_note(title, content)
    
    # Clear the input fields after adding
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    
    messagebox.showinfo("Success", "Note added successfully")
    update_notes_listbox()

#Function to update the Listbox after adding/updating/deleting a note
def update_notes_listbox():
    notes_listbox.delete(0, tk.END)  # Clear the current Listbox
    notes = get_all_note()  # Get all notes from the database
    # Insert each note into the Listbox
    for note in notes:
        notes_listbox.insert(tk.END, f"ID: {note[0]}, Title: {note[1]}")

#Function to delete the selected note from the database
def delete_note():
    try:
        selected_note_index = notes_listbox.curselection()[0]  # Get the index of the selected note
        note_id = notes_listbox.get(selected_note_index).split(",")[0].split(":")[1].strip()  # Extract the ID
        
        delete_note(note_id)  # Delete from the database
        update_notes_listbox()  # Update the Listbox after deletion
        messagebox.showinfo("Success", "Note deleted successfully")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a note to delete")

#Function to update the selected note
def update_note():
    try:
        selected_note_index = notes_listbox.curselection()[0]  # Get the index of the selected note
        note_id = notes_listbox.get(selected_note_index).split(",")[0].split(":")[1].strip()  # Extract the ID
        
        new_title = title_entry.get()
        new_content = content_text.get("1.0", tk.END).strip()
        
        if new_title == "" or new_content == "":
            messagebox.showerror("Input Error", "Please fill out both fields")
            return
        update_note(note_id, new_title, new_content)  # Update the note in the database
        update_notes_listbox()  # Update the Listbox with the new information
        messagebox.showinfo("Success", "Note updated successfully")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a note to update")

#Listbox to display all the notes
notes_listbox = tk.Listbox(root, width=50, height=10)
notes_listbox.pack(pady=20)

#Add buttons for Add, Update, Delete
add_button = tk.Button(root, text="Add Note", command=add_note, bg="#1FED0C", fg="black", font=("Arial", 12))
add_button.pack(pady=10)

update_button = tk.Button(root, text="Update Note", command=update_note, bg="#FFA500", fg="black", font=("Arial", 12))
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Note", command=delete_note, bg="#FF6347", fg="black", font=("Arial", 12))
delete_button.pack(pady=5)

#Initialize the Listbox with current notes
update_notes_listbox()

#Start the Tkinter main loop
root.mainloop()
