# Exercise 1
# Dictionary constructed containing makes and models of several cars.
# Two key value pairs are added and then a menu is presented to allow
# the user to modify one of the existing values.
# 
# Author:       Eamonn Godfrey
# ID:           13214184
# Date:         22/07/21

carsdict = {
    "Nissan" : "Navara",
    "Mitsubishi" : "Lancer",
    "Mazda" : "323",
    "Holden" : "Commodore"
}

#add two values
carsdict["Honda"] = "Civic"
carsdict["Ford"] = "Falcon"

choice = None
while choice != "0":
    print(
        """
        Cars
        
        0 - Quit
        1 - Look up a Make
        2 - Change an Entry
        """
    )

    choice = input("Choice: ")
    print()

    #exit loop
    if choice == "0":
        print("Bye.")
    
    #search and display value
    elif choice == "1":
        term = input("\nWhat Make do you wish to search for? ")
        term = term.capitalize()
        if term in carsdict:
            value = carsdict[term]
            print("\nMake:\t", term, "\nModel:\t", value)
            input("\nPress ENTER to continue...")
        else:
            print("\nSorry, Make ", term, " is not in this list")

    #change a value
    elif choice == "2":
        term = input("\nWhat Make do you wish to change? ")
        term = term.capitalize()
        if term in carsdict:
            value = input("What is the new Model? ")
            value = value.capitalize()
            carsdict[term] = value
            print("\nOkay,", term, "has been redefined")
        else:
            print("\nThat Make doesn't exist")
    else:
        print("\nPlease enter a valid selection")