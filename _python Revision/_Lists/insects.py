# insects.py
# Eamonn Godfrey
# 13214184
# 15/07/21

#create list
insects = ["beetle", "bug", "mayfly", "stonefly", "dragonfly"]

#a. Print the starting list
print("Initial insect list:", insects)

#b. Add a butterfly and a wasp to the list
insects += "butterfly", "wasp"

#c. Print the list with the additions explain the additions in your print-out
print()
print("Adding two more items to insect list...\n", "Insect list:", insects)

#d. Replace the dragonfly with a damselfly
insects[4] = "damselfly"

#e. Print out the result of your replacement-explain replacement
print()
print("Replacing index 4 with damselfly...\n", "Insect list:", insects)

#f. Remove the wasp
del insects[6]

#g. Print your final list. Explain the deletion
print()
print("Deleting wasp from list...\n", "Final insect list:", insects)

#h. Print out the contents of the list using a for loop, they should display vertically. Do display the index numbers
print()
index =-1
print("Insects:")
for item in insects:
    index +=1
    print(index, item)

#i. Print the contents of the list backwards
print()
insects.reverse()
print(insects)