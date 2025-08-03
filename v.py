import json
import tkinter as tk
import time


def add(x):
    with open('w+','history.json') as f:
        datas = json.load(f)
        datas.append(x)
        json.dump(datas,f)

def accessor():
    with open('w+','history.json') as f:
        datas = json.load(f)
        return datas
    
root = tk.Tk()
root.title('J.O.B')

naming = tk.Entry(root,width=40)
naming.pack()

position = tk.Entry(root)
position.pack

status = tk.Entry(root)
status.pack()

search_button = tk.Button(root, text='Search')
search_button.pack()

add_button = tk.Button(root, text='Add')
add_button.pack()

root.mainloop()