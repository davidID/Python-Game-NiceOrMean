nice = 0
mean = 0

def main():
    start()

def start():
    print "Hello an wecome to nice or mean!"
    name = raw_input("What's your name? : ")
    print "Hi and welcome, " + name +"!"
    print "In this game, you will be greeted by several different people. You can treat them nicely or you could be mean."
    print "At the end of the game, your outcome will be determined by how you acted."

    choice = raw_input("Do you want to play? y/n ")

    if choice == "y":
        print "Great, use 'm' for mean and 'n' for nice!"
        begin()

    if choice == "n":
        print "Okay...later!"

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job...you win!"
        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
            print "Okay let's go!"
            nice = 0
            begin()

        if choice == "n":
            print"Say no more...bye!"
            exit()

    if mean > 2:
        print "Too bad! Game over!"
        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
            print "Okay, let's go!"
            mean = 0
            begin()

        if choice == "n":
            print "Off you go!"
            exit()

        elif choice != "y"+"n":
            print "Please enter y or n"

            if choice == "y":
                begin()
            if choice == "n":
                print "See you later!"
                exit()

            if choice != "y"+"n":
                choice = raw_input("Do you want to play? y/n")

    pick = raw_input("Someone approaches you to talk. Will you be nice or mean? n/m ")

    if pick == "n":
        print "They smile, wave and walk away."
        nice = nice+1
        print "You currently have " +str(nice) + " nice."
        begin()
    if pick == "m":
        print "They frown, glare at you and storm off."
        mean = mean+1
        print "You currently have " +str(mean) + " mean."
        begin()
start()
    
