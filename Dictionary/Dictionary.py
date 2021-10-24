#!/usr/bin/env python
# coding: utf-8

# In[17]:


from tkinter import *
from PyDictionary import PyDictionary


# In[20]:


dictionary=PyDictionary()
root=Tk()
root.configure(background='#16E2F5')
root.geometry('500x500')

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))
    
Label(root,text="Dictionary",font=("Helvetica 20 bold"),fg="Green",bg="#16E2F5").pack(pady=10)

frame=Frame(root)
Label(frame,text="Type Word",font=('Helvetica 15 bold'),fg="Green",bg="#16E2F5").pack(side=LEFT)
word=Entry(frame,font=("Helvetica 15 bold"),bg='white')
word.pack()
frame.pack(pady=10)

frame1=Frame(root)
Label(frame1,text="Meaning:- ",font=("Helvetica 10 bold"),bg="#16E2F5").pack(side=LEFT)
meaning=Label(frame1,text="",font=("Helvetica 10"),bg="#16E2F5")
meaning.pack()
frame1.pack(pady=10)

frame2=Frame(root)
Label(frame2,text="Synonym:- ",font=("Helvetica 10 bold"),bg="#16E2F5").pack(side=LEFT)
synonym=Label(frame2,text="",font=("Helvetica 10"),bg="#16E2F5")
synonym.pack()
frame2.pack(pady=10)

frame3=Frame(root)
Label(frame3,text="Antonym:- ",font=("Helvetica 10 bold"),bg="#16E2F5").pack(side=LEFT)
antonym=Label(frame3,text="",font=("Helvetica 10"),bg="#16E2F5")
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root,text="Submit",font=("Helvetica 15 bold"),bg="black",fg="white",command=dict).pack()

root.mainloop()


# In[ ]:




