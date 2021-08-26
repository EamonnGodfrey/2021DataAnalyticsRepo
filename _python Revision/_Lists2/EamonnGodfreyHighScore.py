# Highscores program
# 
# Eamonn Godfrey
# 13214184
# 15/07/21

scores = [(55, "Tim"), (66, "John"), (56, "Fred"), (67, "Tien")]
choice = None
menu =       """

        High Scores 2.0

        0 - Quit
        1 - List Scores
        2 - Add Scores
             
             """


while choice != "0":
    print(menu)
    choice = input("Selection (0, 1, or 2): ")
    print()

    if choice == "0":
        print("Goodbye")

    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did they get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:7]

    else:
        print("Sorry, invalid choice")
input("\n\nPress enter key to exit")
