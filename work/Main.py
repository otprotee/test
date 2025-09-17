import sqlite3
import tkinter as tk

#create tkinter window
root = tk.Tk()
root.geometry("400x250")
root.title('CD Database')


#intalize DB connection
conn = sqlite3.connect('MyCDCollection.db')
cursor_obj = conn.cursor()

# inputs
artist_entry = tk.Entry(root, width=30)
album_entry = tk.Entry(root, width=30)
artist_entry.pack(pady=5)
album_entry.pack(pady=5)
delete_entry = tk.Entry(root, width=30)
delete_entry.pack(pady=5)


# outputs
Add_label = tk.Label(root, text="", anchor="w", justify="left")
Add_label.pack(pady=10)

Select_label = tk.Label(root, text="", anchor="w", justify="left")
Select_label.pack(pady=10)


def AddToTable():


    artist1 = artist_entry.get()
    album1 = album_entry.get()

    cursor_obj.execute('''SELECT album FROM CD''')
    existing = [row[0] for row in cursor_obj.fetchall()]


    if album1 in existing:
        Add_label.config(text="This album is already present")
    else:
        cursor_obj.execute("INSERT INTO CD (artist, album) VALUES (?, ?)", (artist1, album1))
        conn.commit()
        Add_label.config(text="Album added successfully")






def Clean():
    cursor_obj.execute("DELETE FROM CD WHERE artist = ''")
    conn.commit()

def DeleteRecord ():
    delete = delete_entry.get()

    cursor_obj.execute("DELETE FROM CD WHERE artist = ?", (delete,))



def SelectALL ():
    all = '''SELECT * FROM CD'''
    cursor_obj.execute(all)
    output = cursor_obj.fetchall()

    everything_output = ""

    for row in output:
        everything = f"{row[0]}: {row[1]}"
        everything_output += everything + '\n'

    Select_label.config(text=everything_output)
    

add_button = tk.Button(root, text="Add Album", command=AddToTable, )
add_button.pack(pady=5)

select_button = tk.Button(root, text="View database", command=SelectALL)
select_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Record", command=DeleteRecord)
delete_button.pack(pady=5)


#save and exit
root.mainloop()
conn.commit()
conn.close()