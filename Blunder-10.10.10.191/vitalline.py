import sys


linenum = 0
with open(sys.argv[1]) as file_:
    for line in file_:
        linenum += 1
        if "[1;31m" in line:
            print("Line {} :".format(linenum),line,end="")
