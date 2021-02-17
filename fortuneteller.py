fortune1 = ("You will live a happy life")
fortune2 = ("It will rain cats and frogs tomorrow")
fortune3 = ("You will find a winning lottery ticket")
fortune4 = ("Your birthday will occur in less than a year")
fortune5 = ("You will find a large sum of cash")
fortune6 = ("You will receive a promotion")
fortune7 = ("You will have a great bagel")
fortune8 = ("You will undergo traumatic surgery")
set1 = ("Choose a number: 6, 7, 3, 2: ")
set2 = ("Choose a number: 5, 8, 4, 1: ")

prompt1 = input("Shall I tell your fortune? y/n ")
if prompt1 == "y":
    userchoice1 = input("Choose a color: yellow, pink, red, or green: ")
    if userchoice1 == "yellow"  or "pink":
        userchoice2y = input(set1)
        if userchoice2y == "6" or "2":
            userchoice3y6 = input(set1)
            if userchoice3y6 == "6":
                print(fortune6) 
            elif userchoice3y6 == "7":
                print(fortune7) 
            elif userchoice3y6 == "3":
                print(fortune3) 
            elif userchoice3y6 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        elif userchoice2y == "7" or "3":
            userchoice3y7 = input(set2)
            if userchoice3y7 == "5":
                print(fortune5) 
            elif userchoice3y7 == "8":
                print(fortune8) 
            elif userchoice3y7 == "4":
                print(fortune4) 
            elif userchoice3y7 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        else:
            print("That's not a valid response!!")
    elif userchoice1 == "red" or "green":
        userchoice2r = input(set2)
        if userchoice2r == "5" or "2":
            userchoice3r5 = input(set1)
            if userchoice3r5 == "6":
                print(fortune6) 
            elif userchoice3r5 == "7":
                print(fortune7) 
            elif userchoice3r5 == "3":
                print(fortune3) 
            elif userchoice3r5 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        elif userchoice2r == "8" or "4":
            userchoice3r8 = input(set2)
            if userchoice3r8 == "5":
                print(fortune5) 
            elif userchoice3r8 == "8":
                print(fortune8) 
            elif userchoice3r8 == "4":
                print(fortune4) 
            elif userchoice3r8 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        else:
            print("That's not a valid response!!")
    else:
        print("That's not a valid response!!!")
elif prompt1 == "n":
    print("ok, maybe some other time")
else:
    print("That's not a valid response!")
