import json
import tkinter as tk
import datetime


def add(name,position,status):
    x={'company':name,'position':position, 'status':status, 'time':str(datetime.datetime.now())}
    with open('history.json','r+') as f:
        datas = json.load(f)
        datas.append(x)
        f.seek(0)
        f.truncate()
        json.dump(datas,f)

def accessor():
    with open('history.json','r') as f:
        datas = json.load(f)
        return datas

def search(term):
    results=[]
    data= accessor()
    for job in data:
        if job['company']==term:
            results.append(job)
    return results


root = tk.Tk()
root.title('J.O.B')

listbox = tk.Listbox(root, width=80, height=10)
listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky='ns')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

tk.Label(text='Company').grid(row=1, column=0)
naming = tk.Entry(root,width=40)
naming.grid(row=1,column=1)

tk.Label(text='Position').grid(row=2, column=0)
position = tk.Entry(root,width=40)
position.grid(row=2,column=1)

tk.Label(text='Status').grid(row=3, column=0)
status = tk.Entry(root,width=40)
status.grid(row=3,column=1)

search_button = tk.Button(root, text='Search',command=lambda: search(naming.get()))
search_button.grid(row=4,column=1)

add_button = tk.Button(root, text='Add',command=lambda: add(naming.get(),position.get(),status.get()))
add_button.grid(row=4,column=0)

print('')

root.mainloop()