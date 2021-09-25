#!/usr/bin/env python
# coding: utf-8

# In[6]:


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except:
        print("Number Cannot be divided by Zero")
        return 0


def mainmenu():
    print('-'*30)
    print('"1" for add')
    print('"2" for sub')
    print('"3" for multi')
    print('"4" for div')
    print('"5" for user data')
    print('"6" for break')
    print('-'*30)
    
def inputs():
    try:
        a=int(input("enter 1st number:- "))
        b=int(input('enter 2nd number:- '))
    except:
        print("Please Use integer Value")
        a,b=inputs()
    return a,b
    
def main():
    f=open("test.txt",'w')
    f.close()
    while True:
        mainmenu()
        current=datetime.datetime.now()
        c=input("Enter Your choice:- ")
        a,b,h="Some Error","Some Error","Some Error"
        wrong_input=0
        if c=='6':
            string="Date:- "+str(current.date())+", Time:- "+str(current.time())+", Choice:- "+"break\n";
            myfile=open('test.txt','a')    
            myfile.write(string)
            myfile.close()
            break
        if c.isalpha()==True:
            print("Try Again!!")
            string="Date:- "+str(current.date())+", Time:- "+str(current.time())+", Choice:- "+"Wrong input\n";
            myfile=open('test.txt','a')    
            myfile.write(string)
            myfile.close()
            continue
        try:
            if int(c)<5 and int(c)>0:
                a=int(input("enter 1st number:- "))
                b=int(input('enter 2nd number:- '))
        except:
            print("Please Enter integer Value")
            string="Date:- "+str(current.date())+", Time:- "+str(current.time())+", Choice:- "+str(c)+", First Number:- "+str(a)+", Second Number:- "+str(b)+", Result:- "+str(h)+"\n";
            myfile=open('test.txt','a')    
            myfile.write(string)
            myfile.close()
            a,b=inputs()
        if c=='1':
            h=add(a,b)
            print("The addition is:- ",h)
        elif c=='2':
            h=sub(a,b)
            print("The subtraction is:- ",h)
        elif c=='3':
            h=multi(a,b)
            print("The multiplication is:- ",h)
        elif c=='4':
            h=div(a,b)
            print("The division is:- ",h)
        elif c=='5':
            found=0
            myfile=open('test.txt','r')
            for i in myfile:
                print(i)
                found=1
            if found==0:
                print("Record not found")
            myfile.close()
            continue
        else:
            print("Wrong input | Try again")
            wrong_input=1
        string="Date:- "+str(current.date())+", Time:- "+str(current.time())+", Choice:- "+str(c)+", First Number:- "+str(a)+", Second Number:- "+str(b)+", Result:- "+str(h)+"\n";
        myfile=open('test.txt','a')    
        myfile.write(string)
        myfile.close()
        if wrong_input==1:
            continue
        ch=input("Do you want to do more operations Y|N:- ")
        if ch in 'Nn':
            break

import datetime            
main()            


# In[ ]:




