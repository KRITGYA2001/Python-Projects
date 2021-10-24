#!/usr/bin/env python
# coding: utf-8

# In[44]:


from tkinter import *
from tkinter import messagebox


# In[45]:


tasks_list=[]
counter=1
def inputError():
    if enterTaskField.get()=="":
        messagebox.showerror("Input Error")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0,END)
    
def clear_taskField():
    enterTaskField.delete(0,END)    


# In[46]:


def insertTask():
    global counter
    value=inputError()
    if value==0:
        return
    content=enterTaskField.get()+"\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars',"[ "+str(counter)+" ] "+content)
    counter+=1
    clear_taskField()


# In[47]:


def delete():
    global counter
    if len(tasks_list)==0:
        messagebox.showerror("No task")
        return
    number=taskNumberField.get(1.0,END)
    if number=="\n":
        messagebox.showerror("input error")
        return
    else:
        task_no=int(number)
    clear_taskNumberField()
    tasks_list.pop(task_no-1)
    counter-=1
    TextArea.delete(1.0,END)
    
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars','[ '+str(i+1)+" ]"+tasks_list[i])


# In[50]:


if __name__=="__main__":
    gui=Tk()
    gui.configure(background='#728FCE')
    gui.title("TODO App")
    gui.geometry('250x300')
    enterTask=Label(gui,text="Enter Your Task",background='#728FCE',fg="white",font="10")
    enterTaskField=Entry(gui,background="white")
    Submit=Button(gui,text="Submit",fg="white",bg="black",command=insertTask)
    TextArea=Text(gui,height=5,width=25,font="lucida 13",background="white",fg="black")
    taskNumber=Label(gui,text="Delete Task Number",bg="#728FCE",fg="white")
    taskNumberField=Text(gui,height=1,width=2,font="lucida 13",background="white")
    delete=Button(gui,text="Delete",fg='white',bg="black",command=delete)
    Exit=Button(gui,text="Exit",fg='white',bg='red',command=gui.destroy)
    enterTask.grid(row=0,column=2)
    enterTaskField.grid(row=1,column=2,ipadx=50)
    Submit.grid(row=3,column=2)
    TextArea.grid(row=5,column=2,padx=10,sticky=W)
    taskNumber.grid(row=6,column=2,pady=5)
    taskNumberField.grid(row=7,column=2)
    delete.grid(row=8,column=2,pady=5)
    Exit.grid(row=9,column=2)
    gui.mainloop()    


# In[ ]:




