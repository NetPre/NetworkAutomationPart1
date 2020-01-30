


with open("./TEXT/TheBigfile.txt") as fileobject:
    for line in fileobject:
        if(' line protocol' in line):
            print(line)

