import random


file1 = open('things.txt', 'r')
Lines = file1.readlines()

linesNum = len(Lines)
random = random.randint(0,linesNum - 1)

print("suggesstion: {}".format(Lines[random]))
