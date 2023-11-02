# import os.path

PATH = "C:\\Users\\User\\Downloads\\Uni\\1st Sem\\Structured Algorithm & Programming\\Codes\\Lecture\\Week 9\\FreePalestine.txt"

# if os.path.isfile(PATH):
#     print("This file exist")

# fileOpen = open(PATH, "w")

# fileOpen.write("Hello\n")
# fileOpen.write("World!")

# fileOpen.close()

fileOpen = open(PATH, "r")

print(fileOpen.readlines())

fileOpen.close()
