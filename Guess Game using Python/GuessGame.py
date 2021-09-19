#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os
from time import sleep
from random import randint

def gameMenu(): 
    print('             Hello               ')
    print('    Welcome to Guess Number     ')
    print('             Game               ')
    print('*'*35)
    print("Lets see the rules")
    print('1)Choose the range in which a random number will be choosen')
    print('2)For every wrong guess we deduct 5 from score')
    print('3)Total score is 100')
    print('4)You loose if score is below 20')
    print('*'*35)
    
def choicesmenu():
    print(' ------------------------------')
    print('   Are You Ready to Play...?  ')
    print('   Press "1" to Start Game    ')
    print('   Press "2" to Quit Game     ')
    print(' ------------------------------')
   
    
def update(lst,a,name,score):
    for i in lst:
        if i[1]==a:
            i[1]=str(score)
            i[0]=name
            break
    f=open('GuessGame.txt','w')        
    for i in lst:
        name=i[0]
        score=i[1]
        string="{} {}\n".format(name,score)
        f.write(string)
    f.close()         
    
def minscore():
    lst=[]
    f=open('GuessGame.txt','r')
    for i in range(5):
        q=f.readline()
        q=q.split()
        lst.append(q[1])
    f.close()
    return min(lst)    

def inputdata(name,score):
    f=open('GuessGame.txt','a')
    string="{} {}\n".format(name,score)
    f.write(string)
    f.close()
    
def data():
    lst=[]
    f=open('GuessGame.txt','r')
    for i in range(5):
        q=f.readline()
        q=q.split()
        lst.append(q)
    f.close()
    return lst    
    
def countdata():
    a=open('GuessGame.txt','r')
    s=a.readline()
    count=1
    while s:
        count+=1
        s=a.readline()
    return count-1

 
    
def main():
    a=1
    while True:
        if a==1:
            gameMenu()
        choicesmenu()
        ch=input("\nEnter Your Choice:- ")
        os.system('cls')
        if ch=='2':
            sleep(1)
            print("Exiting",end="")
            i='.'
            for _ in range(7):
                print(i,end="")
                sleep(0.25)
            print("")      
            os.system('cls')
            sleep(1)
            print("Thanku for playing")
            print("Bye, See you soon")
            break
        if ch=='1':
            print("Let's Gooooooo")
            sleep(1)
            os.system('cls')
            print("Starting",end="")
            i='.'
            for _ in range(7):
                print(i,end="")
                sleep(0.25) 
            print("")    
            os.system('cls')
            a=1
            game()
        else:
            os.system('cls')
            print("Wrong Input|Try Again")
            sleep(2)
            os.system('cls')
            a=0
            continue
        break    


            
def rangeinputs():
    try:
        Lowrange =int(input("Enter Starting range:- "))
        Highrange =int(input("Enter Ending range:- "))
        if Lowrange>Highrange:
            os.system('cls')
            print("High Range Cannot be smaller than lower range :(")
            sleep(1.2)
            print("Try Again!!")
            sleep(1)
            os.system('cls')
            Lowrange,Highrange=rangeinputs()
    except:
        os.system('cls')
        Lowrange,Highrange=rangeinputs()
    return Lowrange,Highrange

def guessinputs():
    try:
        Guessno=int(input('Please enter your guess number:- '))
    except:
        os.system('cls')
        Guessno=guessinputs()
    return Guessno             

def names():
    try:
        name=input("Enter Your Name:- ")
    except:
        os.system('cls')
        print("Please Enter Valid Name")
        os.system('cls')
        name=names()
    return name    
    
def game():
    name=names()
    os.system('cls')
    Lrange,Hrange=rangeinputs()
    found,rnum,score=0,0,100
    sleep(1)
    os.system('cls')
    print('The number will be from an  range of {0} to {1}'.format(Lrange,Hrange))
    Gnum=guessinputs()
    rnum=randint(Lrange,Hrange)
    while Gnum!=rnum:
        score=score-5
        if(score<20):
            print("You Lost the game.")
            found=1
            break
        if Gnum>rnum:
            print("Try something low")   
        if Gnum<rnum:
            print("Try something high")
        print("Score:-",score)
        sleep(1.5)
        os.system('cls')
        Gnum=guessinputs()     
    if found==0:  
        sleep(1.5)
        os.system('cls')
        print('Congratulations! you guessed the number.')
        print("Your Score is:- ",score)
    else:
        print("Your Score is:-",score)
    if(countdata()<5):
        inputdata(name,score)
    else:    
        lst=data()
        mins=minscore()
        update(lst,mins,name,score)
    sleep(1.5)
    print('\n\nReturning you to the menu...')
    sleep(1.2)
    os.system('cls')
    main()           
    

os.system('cls')
main()    

