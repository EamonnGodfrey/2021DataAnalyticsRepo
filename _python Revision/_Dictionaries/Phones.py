# Exercise 2
# Dictionary constructed containing brands and models of phones as
# records. The user is presented a menu where they can modify the 
# models of the brands, delete a brand, or add a brand
# 
# Author:       Eamonn Godfrey
# ID:           13214184
# Date:         22/07/21
import pprint

phonebrands = {
    "Apple" : "iPhone 12 Pro Max",
    "Samsung" : "Galaxy S21 Ultra",
    "OnePlus" : "9 Pro",
    "Google" : "Pixel 4a",
    "Motorola" : "Moto G Power"
}

choice = None
while choice != "0":
    print(
        """
        Phones
        
        0 - Quit
        1 - List All
        2 - Look up a Phone
        3 - Add an Entry
        4 - Change an Entry
        5 - Delete an Entry
        """
    )

    choice = input("Choice: ")
    print()

    #exit loop
    if choice == "0":
        print("Bye.")

    elif choice == "1":
        pprint.pprint(phonebrands)
    
    #search and display value
    elif choice == "2":
        term = input("\nWhat phone brand do you wish to search for? ")
        if term in phonebrands:
            value = phonebrands[term]
            print("\nBrand:\t", term, "\nModel:\t", value)
            input("\nPress ENTER to continue...")
        else:
            print("\nSorry, Brand ", term, " is not in this list")
            input("\nPress ENTER to continue...")

    #add a value
    elif choice == "3":
        term = input("What Brand of phone do you wish to add? ")
        if term not in phonebrands:
            value = input("What is the Model of this phone? ")
            phonebrands[term] = value
            print("\n", term, value, "has been added.")
            input("\nPress ENTER to continue...")

        else:
            print("\nThat Make already exists. Try changing the existing entry.")
            input("\nPress ENTER to continue...")
        
    #change a value
    elif choice == "4":
        term = input("\nWhat Brand do you wish to change? ")
        if term in phonebrands:
            value = input("What is the new Model? ")
            phonebrands[term] = value
            print("\nOkay,", term, "has been redefined")
            input("\nPress ENTER to continue...")
        else:
            print("\nThat Make doesn't exist")
            input("\nPress ENTER to continue...")
    
    elif choice == "5":
        term = input("\nWhich Brand do you want to delete? ")
        if term in phonebrands:
            del phonebrands[term]
            print("\nPhone brand", term, "deleted.")
            input("Press ENTER to continue...")
        else:
            print("\nPhone brand", term, "does not exist in this dictionary.")
            input("\nPress ENTER to continue...")
    else:
        print("\nPlease enter a valid selection.")
        input("\nPress ENTER to continue...")
