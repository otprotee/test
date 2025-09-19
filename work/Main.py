import sqlite3
import tkinter as tk
import time

#create tkinter window
root = tk.Tk()
root.geometry("400x500")
root.title('CD Database')
root.config(bg="black")

#item names
def on_entry_click_artist(event):
    artist_entry.delete(0, "end")

def on_entry_click_album(event):
    album_entry.delete(0, "end")

def del_artist(event):
    delete_entry.delete(0, "end")

def del_album(event):
    delete_entry_album.delete(0, "end")



#entry
artist_entry = tk.Entry(root, width=30)
artist_entry.insert(0, "artist name add")
artist_entry.bind("<FocusIn>", on_entry_click_artist)
artist_entry.pack(pady=5)

album_entry = tk.Entry(root, width=30)
album_entry.insert(0, "album name add")
album_entry.bind("<FocusIn>", on_entry_click_album)
album_entry.pack(pady=5)

delete_entry = tk.Entry(root, width=30)
delete_entry.insert(0, "artist name delete")
delete_entry.bind("<FocusIn>", del_artist)
delete_entry.pack(pady=5)

delete_entry_album = tk.Entry(root, width=30)
delete_entry_album.insert(0, "album name delete")
delete_entry_album.bind("<FocusIn>", del_album)
delete_entry_album.pack()

#intalize DB connection
conn = sqlite3.connect('MyCDCollection.db')
cursor_obj = conn.cursor()




# outputs
Add_label = tk.Label(root,fg="white", bg="black", text="", anchor="w", justify="left")
Add_label.pack(pady=10)

Select_label = tk.Label(root,fg="white", bg="black", text="", anchor="w", justify="left")
Select_label.pack(side="bottom")

delete_label = tk.Label(root,fg="white", bg="black", text="", anchor="w", justify="left")
delete_label.pack(pady=10)


def AddToTable():

    artist1 = artist_entry.get()
    album1 = album_entry.get()


    cursor_obj.execute('''SELECT album FROM CD''')
    existing = [row[0] for row in cursor_obj.fetchall()]


    if album1 in existing:
        Add_label.config(text="This album is already present")
    elif album1 == "album name add" or artist1 == "artist name add":
        print()
    else:
        cursor_obj.execute("INSERT INTO CD (artist, album) VALUES (?, ?)", (artist1, album1))
        conn.commit()
        Add_label.config(text="Album added successfully")
    conn.commit()


def Clean():
    cursor_obj.execute("DELETE FROM CD WHERE artist = ''")
    conn.commit()


def DeleteSubmit ():
    delete = delete_entry.get()
    delete = str(delete)
    cursor_obj.execute("DELETE FROM CD WHERE artist = ?", (delete,))
    conn.commit()
    delete_label.config(text="Record successfully deleted")


def SelectALL ():
    all = '''SELECT * FROM CD'''
    cursor_obj.execute(all)
    output = cursor_obj.fetchall()

    everything_output = ""

    for row in output:
        everything = f"{row[0]} : {row[1]}"
        everything_output += everything + '\n'

    Select_label.config(text=everything_output)


add_button = tk.Button(root, text="Add Album", command=AddToTable, )
add_button.pack(pady=5)

select_button = tk.Button(root, text="View database", command=SelectALL)
select_button.pack(pady=5)


delete_button = tk.Button(root, text="Delete Record", command=DeleteSubmit)
delete_button.pack(pady=5)


#save and exit
root.mainloop()
conn.commit()
conn.close()