#Import modules
import os
from lib import Functions
#exec(open('./lib/Functions.py').read())

run = "y"

while run == "y":
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")

        Functions.splitcsv()

        print("\n\n\nEnd of program. Would you like to run another task?")
        print("(Y/N) ", end="")
        run = input().lower()

