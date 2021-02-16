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
    if userchoice1 == "yellow":
        userchoice2y = input(set1)
        if userchoice2y == "6":
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
        if userchoice2y == "7":
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
        if userchoice2y == "3":
            userchoice3y3 = input(set2)
            if userchoice3y3 == "5":
                print(fortune5) 
            elif userchoice3y3 == "8":
                print(fortune8) 
            elif userchoice3y3 == "4":
                print(fortune4) 
            elif userchoice3y3 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        if userchoice2y == "2":
            userchoice3y2 = input(set1)
            if userchoice3y2 == "6":
                print(fortune6) 
            elif userchoice3y2 == "7":
                print(fortune7) 
            elif userchoice3y2 == "3":
                print(fortune3) 
            elif userchoice3y2 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        else:
            print("That's not a valid response!!")
    elif userchoice1 == "pink":
        userchoice2p = input(set1)
        if userchoice2p == "6":
            userchoice3p6 = input(set1)
            if userchoice3p6 == "6":
                print(fortune6) 
            elif userchoice3p6 == "7":
                print(fortune7) 
            elif userchoice3p6 == "3":
                print(fortune3) 
            elif userchoice3p6 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        elif userchoice2p == "7":
            userchoice3p7 = input(set2)
            if userchoice3p7 == "5":
                print(fortune5) 
            elif userchoice3p7 == "8":
                print(fortune8) 
            elif userchoice3p7 == "4":
                print(fortune4) 
            elif userchoice3p7 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        elif userchoice2p == "3":
            userchoice3p3 = input(set2)
            if userchoice3p3 == "5":
                print(fortune5) 
            elif userchoice3p3 == "8":
                print(fortune8) 
            elif userchoice3p3 == "4":
                print(fortune4) 
            elif userchoice3p3 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        if userchoice2p == "2":
            userchoice3p2 = input(set1)
            if userchoice3p2 == "6":
                print(fortune6) 
            elif userchoice3p2 == "7":
                print(fortune7) 
            elif userchoice3p2 == "3":
                print(fortune3) 
            elif userchoice3p2 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        else:
            print("That's not a valid response!!")
    elif userchoice1 == "red":
        userchoice2r = input(set2)
        if userchoice2r == "5":
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
        elif userchoice2r == "8":
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
        elif userchoice2r == "4":
            userchoice3r4 = input(set2)
            if userchoice3r4 == "5":
                print(fortune5) 
            elif userchoice3r4 == "8":
                print(fortune8) 
            elif userchoice3r4 == "4":
                print(fortune4) 
            elif userchoice3r4 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        if userchoice2r == "2":
            userchoice3r2 = input(set1)
            if userchoice3r2 == "1":
                print(fortune6) 
            elif userchoice3r2 == "7":
                print(fortune7) 
            elif userchoice3r2 == "3":
                print(fortune3) 
            elif userchoice3r2 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        else:
            print("That's not a valid response!!")
    elif userchoice1 == "green":
        userchoice2g = input(set2)
        if userchoice2g == "5":
            userchoice3g5 = input(set1)
            if userchoice3g5 == "6":
                print(fortune6) 
            elif userchoice3g5 == "7":
                print(fortune7) 
            elif userchoice3g5 == "3":
                print(fortune3) 
            elif userchoice3g5 == "2":
                print(fortune2) 
            else:
                print("That's not a valid response!!")
        elif userchoice2g == "8":
            userchoice3g8 = input(set2)
            if userchoice3g8 == "5":
                print(fortune5) 
            elif userchoice3g8 == "8":
                print(fortune8) 
            elif userchoice3g8 == "4":
                print(fortune4) 
            elif userchoice3g8 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        elif userchoice2p == "4":
            userchoice3g4 = input(set2)
            if userchoice3g4 == "5":
                print(fortune5) 
            elif userchoice3g4 == "8":
                print(fortune8) 
            elif userchoice3g4 == "4":
                print(fortune4) 
            elif userchoice3g4 == "1":
                print(fortune1) 
            else:
                print("That's not a valid response!!")
        elif userchoice2g == "2":
            userchoice3g2 = input(set1)
            if userchoice3g2 == "1":
                print(fortune6) 
            elif userchoice3g2 == "7":
                print(fortune7) 
            elif userchoice3g2 == "3":
                print(fortune3) 
            elif userchoice3g2 == "2":
                print(fortune2) 
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





