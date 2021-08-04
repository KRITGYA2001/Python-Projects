#!/usr/bin/env python
# coding: utf-8

# # ATM MACHINE

# In[2]:


pin_code = 1234
amount = 10000
acc_no = 1234567
acc_holder_name = "JACK"
print("SWIPE YOUR CARD")
pc = int(input("ENTER YOUR PIN CODE : "))
if pin_code == pc:
    while(True):
        print("1. WITHDRAW MONEY")
        print("2. TRANSFER MONEY")
        print("3. BALANCE ENQURY")
        print("4. CHANGE PIN CODE")
        print("5. EXIT")
        choice = int(input("ENTER YOUR CHOICE : "))
        if choice == 1:
            amt = int(input("ENTER THE AMOUNT : "))
            if amt > amount:
                print("\n")
                print("ENTER VALID AMOUNT")
                print("\n\n")
            else:
                print("\n")
                print("TRANSACTION IS SUCCESSFUL")
                print("\n\n")
                amount = amount - amt
        elif choice == 2:
            a_num = int(input("ENTER THE ACCOUNT NUMBER : "))
            a_name = input("ENTER THE NAME OF ACCOUNT HOLDER : ")
            if a_num == acc_no and a_name == acc_holder_name:
                amt_to_trans = int(input("ENTER THE AMOUNT TO BE TRANSFER : "))
                print("\n")
                if amount >= amt_to_trans:
                    print("TRANSITION IS SUCCESSFUL")
                    print("\n")
                    amount = amount - amt_to_trans
                else:
                    print("ENTER A VALID AMOUNT")
                    print("\n")
            else:
                print("\n")
                print("INVALID ACCOUNT NUMBER OR NAME")
                print("\n\n")
        elif choice == 3:
            print("\n")
            print("TOTAL AMOUNT PRESENT IS : ",amount)
            print("\n\n")
        elif choice == 4:
            resent_pin_code = int(input("ENTER YOUR RECENT PIN CODE : "))
            if resent_pin_code == pin_code:
                print("ENTER YOUR NEW PIN CODE")
                new_pincode = int(input(""))
                pin_code = new_pincode
                print("\n")
                print("PIN CODE GOT CHANGE SUCCESSFULLY")
                print("FOR COUNTINUING START FROM STARTING AS YOUR PIN CODE GOT UPDATED")
                print("THANK YOU")
                break
            else:
                print("\n")
                print("ENVALID PIN CODE")
                print("\n\n")
        else:
            exit()
else:
    print("WRONG PIN CODE ")

