#User name varification And pin check
#THIS IS A BANK MANAGEMENT SYSTEM I BUILT HOPE YOU LIKE IT !!
import sys

print("VALID USERNAMES:-\nNevvil sir\nRushil\nSathvik\nNiksh\nAdvaith\nPriangi")
user = str(input("Enter your name:- "))

bal = int()



no = 1
yes = 0

balns = int(4000)
balr = int(4000)
bals = int(4000)
baln = int(4000)
bala = int(4000)
balp = int(4000)

if user == "Nevvil sir":

    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(balns)
        print("Bal of account :-",balns,"₹")
    else :
        print("Invalid pin")
    fail = no 
elif user == "Rushil":
    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(balr)
        print("Bal of account :-",balr,"₹")
    else :
        print("Invalid pin")
    fail = no 
elif user == "Sathvik":
    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(bals)
        print("Bal of account :-",bals,"₹")
    else :
        print("Invalid pin")
    fail = no 
elif user == "Niksh":
    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(baln)
        print("Bal of account :-",baln,"₹")
    else :
        print("Invalid pin")
    fail = no 
elif user == "Advaith":
    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(bala)
        print("Bal of account :-",bala,"₹")
    else :
        print("Invalid pin")
    fail = no 
elif user == "Priangi":
    pin = int(input("Enter your pin:- "))
    if pin == 1234:
        bal = int(balp)
        print("Bal of account :-",balp,"₹")
    else :
        print("Invalid pin")
    fail = yes 
else:
    print("Invalid user")
    fail = yes 

# withdraw , deposit ,balence 

action = ""

i = 1

if fail == no :
    for i in range (10):
        if bal == 0:
            print("No money")
        action = int(input("PRESS THE BELOW NUMBER TO DO VARIOUS THING'S \nPress 1 to withdraw \nPress 2 deposit \nPress 3 to check your current ballence\nPress 4 to transfer some money to an other account\nPress 5 to exit\n:- "))
        if action == 1 :
            withdraw = int(input("Enter the amount you want to withdraw:- "))
            bal = int(bal - withdraw)
            print("Done Bal =",bal)
            if withdraw >= bal:
                print("Not enough money !!!")

        elif action == 2 :
            deposit = int(input("Enter the amount you want to deposit:- "))
            bal = int(bal + deposit)
            print("Done Bal =",bal)
        elif action == 3 :
            if user == "Nevvil sir":
               print(balns) 
            elif user == "Rushil":
                print(balr)       
            elif user == "Sathvik":
                print(bals)
            elif user == "Niksh":
                print(baln)  
            elif user == "Advaith":
                print(bala)
            elif user == "Priangi":
                print(balp)
            else :
                print() 
        elif action == 4:
            user2 = str(input("Enter the account who want to transfer the money to :- "))
            amount2 = int(input("Enter the amount you want to transfer:- "))
            if user2 == "Nevvil sir":
                print("Ballance of",user2,"account is:- ",balns)
                print("Now the ballance of ",user2,"is",balns + amount2) 
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print() 
            elif user2 == "Rushil":
                print("Ballance of",user2,"account  is:- ",balr) 
                print("Now the ballance of ",user2,"is",balns+amount2)
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print()       
            elif user2 == "Sathvik":
                print("Ballance of",user2," account is:- ",bals)
                print("Now the ballance of ",user2,"is",balns+amount2)
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print() 
            elif user2 == "Niksh":
                print("Ballance of",user2," account is:- ",baln)  
                print("Now the ballance of ",user2,"is",baln+amount2)
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print() 
            elif user2 == "Advaith":
                print("Ballance of",user2,"account is:- ",bala)
                print("Now the ballance of ",user2,"is",balns+amount2)
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0 :
                        print("too much money")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print() 
            elif user2 == "Priangi":
                print("Ballance of",user2,"account is:- ",balp)
                print("Now the ballance of ",user2,"is",balns+amount2)
                if user == "Nevvil sir":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence") 
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Rushil":
                    if bal - amount2 > 0 :
                        bal = bal-amount2
                        print(bal,"is your ballence")       
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Sathvik":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Niksh":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")  
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Advaith":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                elif user == "Priangi":
                    if bal - amount2 > 0 :
                        bal = bal - amount2
                        print(bal,"is your ballence")
                    elif bal - amount2 < 0:
                        print("Too much money you do not have that much ")
                else :
                    print() 
            else:
                print("")


        elif action == 5:
            print("OK EXITING BANK PLEASE VISIT AGAIN BYE ") 
            i=i+100000     
            sys.exit() 
        else:
            print()
        i=i-1        
elif fail == yes:
    fail = yes
else:
    fail = yes
