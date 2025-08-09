import json
import tkinter as tk
import datetime

global indexx
indexx =None
def add(name,position,status):
    x={'company':name,'position':position, 'status':status, 'time':str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))}
    with open('C:/Users/lodar/Desktop/Python/Follower/history.json','r+') as f:
        datas = json.load(f)
        datas.append(x)
        f.seek(0)
        f.truncate()
        json.dump(datas,f)
    search('')
    len_updater()

def accessor():
    with open('C:/Users/lodar/Desktop/Python/Follower/history.json','r') as f:
        datas = json.load(f)
        return datas

def search(term):
    results=[]
    listbox.delete(0, tk.END)  
    data= accessor()
    for job in data:
        if term in job['company']:
            results.append(job)
            listbox.insert(tk.END, f"{job['company']} | {job['position']} | {job['status']} | {job['time']}")
            print(job)
    return results

def len_updater():
    x=len(accessor())
    counter.config(text=f'{x}')
    return x

def field_updater(index):
    data=accessor()
    item=data[index]
    naming.delete(0,tk.END)
    position.delete(0,tk.END)
    status.delete(0,tk.END)
    naming.insert(0,f'{item['company']}')
    position.insert(0,f'{item['position']}')
    status.insert(0,f'{item['status']}')

def on_select(e):
    widget = e.widget
    selection = widget.curselection()
    if selection:
        index=selection[0]
        global indexx
        indexx=index
        field_updater(index)

def item_updater():
    data = accessor()
    data[indexx]['company']=naming.get()
    data[indexx]['status']=status.get()
    data[indexx]['position']=position.get()
    print(data)
    with open('C:/Users/lodar/Desktop/Python/Follower/history.json','r+') as f:
        f.seek(0)
        f.truncate()
        json.dump(data,f)
    search('')


root = tk.Tk()
root.title('J.O.B')

listbox = tk.Listbox(root, width=80, height=10)
listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky='ns')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.bind("<<ListboxSelect>>", on_select)

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

update_button = tk.Button(root,text='Update', command=lambda:item_updater())
update_button.grid(row=5,column=1)

counter = tk.Label(text=f'0')
counter.grid(row=5,column=0)
len_updater()
search('')

root.mainloop()