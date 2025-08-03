import json
import tkinter as tk
import datetime


def add(name,position,status):
    x={'company':name,'position':position, 'status':status, 'time':str(datetime.datetime.now())}
    with open('history.json','w+') as f:
        datas = json.loads(f)
        datas.append(x)
        json.dump(datas,f)

def accessor():
    with open('w+','history.json') as f:
        datas = json.load(f)
        return datas
    
root = tk.Tk()
root.title('J.O.B')

tk.Label(text='Company').grid(row=0, column=0)
naming = tk.Entry(root,width=40)
naming.grid(row=0,column=1)

tk.Label(text='Position').grid(row=1, column=0)
position = tk.Entry(root,width=40)
position.grid(row=1,column=1)

tk.Label(text='Position').grid(row=2, column=0)
status = tk.Entry(root,width=40)
status.grid(row=2,column=1)

search_button = tk.Button(root, text='Search')
search_button.grid(row=3,column=1)

add_button = tk.Button(root, text='Add',command=lambda: add(naming.get(),position.get(),status.get()))
add_button.grid(row=3,column=0)

print('')

root.mainloop()