import random
file = "GuessNum/bestscore.txt"
def loadscore():
    global bestscore
    with open(file) as f:
        try:
            bestscore = int(f.read())
        except ValueError:
            bestscore = ""

def viewscore():
    if bestscore == "":
        print("No best score yet. Play the game to set a new score.")
    else:
        print("-------------------------------")
        print(f"The lowest number of guesses ever recorded by you are {bestscore}.")
        print("-------------------------------")
        main()

guesses = 0

def play():
    while True:
        num = random.randint(1, 100)
        usernum = -1
        while usernum != num:
            try:
                usernum = int(input("Guess the number (1-100): "))
            except ValueError:
                print("Please enter digits only! Its a number you idiot!")
                return
            if usernum > num:
                print("Lower!")
            elif usernum < num:
                print("Higher!")
            global guesses
            guesses += 1
        print("-------------------------------")
        print(f"You guessed it! It was {num}. It took you {guesses} tries.")
        print("-------------------------------")
        if bestscore == "":
            print(f"Congrats! You just set a new record of {guesses} tries!")
            with open(file, "w") as f:
                f.write(str(guesses))
            loadscore()
        else:
            if guesses > bestscore:
                print(f"Try to beat {bestscore} next time.")
            elif guesses < bestscore:
                print(f"Congrats! You just set a new record of {guesses} tries!")
                with open(file, "w") as f:
                    f.write(str(guesses))
                loadscore()
        print("-------------------------------")
        print("1. Play Again\n2. Main Menu\n3. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a digit.")
        if choice == 1:
            play()
        elif choice == 2:
            main()
        elif choice == 3:
            print("Quitting GuessNum...")
            exit()
        else:
            print("Invalid input. Please try again.")
            return

def main():
    while True:
        print("■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■■■■■■- GuessNum -■■■■■■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■")
        print("1. Play\n2. View best score\n3. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("")
            break
        if choice == 1:
            play()
        elif choice == 2:
            viewscore()
        elif choice == 3:
            print("Quitting GuessNum...")
            exit()
        else:
            print("Invalid input. Please try again.")
            return

loadscore()
main()