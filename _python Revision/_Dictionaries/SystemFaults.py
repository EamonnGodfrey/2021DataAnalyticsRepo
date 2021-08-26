# Exercise 3
# Dictionary constructed containing common network faults and a simple
# description on how to resolve them. The user will be able to search
# the dictionary for these faults which will return the fix.
# 
# Author:       Eamonn Godfrey
# ID:           13214184
# Date:         22/07/21


networkFaults = {
    "Duplicate IP Addresses" : "Disable DHCP on the new device. Vet your static IP distribution. Configure router to assign DHCP in the upper end of your subnet.",
    "IP Address Exhaustion" : "Default address pool of your router could have run out of addresses. Access DHCP settings on your router and adjust the size of the address pool.",
    "DNS Problems" : "Configure network device to use own DNS server, checking 'Internet Protocol Version 4 (TCP/IP)' settings will show if an incorrect DNS server is specified.",
    "Unable to Connect to Network" : "Eliminate obvious barriers such as a bad cord, poor WiFi signal, drivers etc. Ensure the network adapter is configured correctly.",
    "Local Network Cannot Connect to the Internet" : "Reboot router and modem. Use tracrt utility to identify communication breaks.",
    "Slow Internet Performance" : "Use speed test websites, testing from geographically remote servers. Configure a wired connection if possible."
}

choice = None
while choice != "0":
    print(
        """
        Network Help
        
        0 - Quit
        1 - List Faults
        2 - Look up a Fix
1
        """
    )

    choice = input("Choice: ")
    print()

    #exit loop
    if choice == "0":
        print("Bye.")

    elif choice == "1":
        for x in networkFaults:
            print(x)
        input("\nPress ENTER to continue...")
    #search and display value
    elif choice == "2":
        term = input("\nWhich Fault do you wish to view? ")
        if term in networkFaults:
            value = networkFaults[term]
            print("Fix:\t", value)
            input("\nPress ENTER to continue...")
        else:
            print("\nSorry, Fault ", term, " is not in this list")
            input("\nPress ENTER to continue...")
    else:
        print("\nPlease enter a valid selection.")
        input("\nPress ENTER to continue...")
