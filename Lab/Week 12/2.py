"""1"""

# the code will create the file variable to open and write to a file
# name pantun.txt. File will be created in your compiler.
outfile = open(
    r"C:\Users\User\Downloads\Uni\1st Sem\Structured Algorithm & Programming\Codes\Lab\Week 12\pantun.txt", "w")
# 1st line
outfile.write('buai laju laju\n')
# second line
outfile.write('sampai pokok sena\n')
# third line
outfile.write('apa dalam baju\n')
# display on console to notify the user that the data is save
print("file has successfully created")
outfile.close()


"""2"""

# the code will create the file variable to open and read from a file
# name pantun.txt. File was created in your compiler earlier.
infile = open(
    r"C:\Users\User\Downloads\Uni\1st Sem\Structured Algorithm & Programming\Codes\Lab\Week 12\pantun.txt", "r")
# read the content of the file and store it the variable, content
content = infile.readlines()
# display the value in content line by line
for line in content:
    print(line)
# display on console the notification that data is transferred
print("file has successfully transferred")
infile.close()


"""3"""

# the code will create the file variable to open file and append
# additional data to a file name pantun.txt. File was created in your
# compiler earlier.
outfile = open(
    r"C:\Users\User\Downloads\Uni\1st Sem\Structured Algorithm & Programming\Codes\Lab\Week 12\pantun.txt", "a")
# 4th line
outfile.write('sekuntum bunga cina\n')
# display on console to notify the user that the data is save
print("file has successfully edited")
outfile.close()
