import random
def guesss_num(): #function for guessing the number
    print("Try to guess that number")
    for i in range(1,4): #Run for 3 times
        print("Enter the number between 1 to 50 ")
        global guess
        guess=int(input("Enter the number:"))
        if(guess>secretnumber):
            print("Number is too high")
        elif(guess<secretnumber):
            print("Number is too low")
        else:
            break
choice=input("You want to play?")
while(choice == "yes"):
    print("I am Currently Thinking of a number")
    secretnumber=random.randint(1,50) #Creates a random integer
    guesss_num()
    if(guess== secretnumber):
        print("Congratulations!! You guessed it right ")
    else:
        print("Better Luck next time ")
        print("The actual number was "+str(secretnumber)) #says what was the number
    choice=input("You Want to Continue?")
else:
    exit()