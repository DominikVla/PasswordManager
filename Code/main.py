# Imports
import re
from time import sleep



# Choice for what the application does this session
choice = "n/a"

# While loop for user decision
while choice !="r" or choice !="a":
    print ("Do you want to add a password(a) or read passwords(r)?")
    choice = input()
    if choice =="r" or choice =="a":
        break

# Takes user input and stores it
if choice =="a":
    f = open("Password.txt", "a")
    Application = input("Name of Application: ")
    Pass = input("Password: ")
    add = Application ,"=", Pass
    add = str(add)
    f.write(f"{add}\n")
    f.close()
    print("Password Stored!")
    sleep(3)

# Reads out all passwords
elif choice=="r":
    try:
        with open("Password.txt", "r") as f:
            text = f.read()
            patn = re.sub(r"[\([{',})\]]", "", text) # Removes unneeded characters
            print (patn)
            sleep (500)
    except:
        print("No passwords have been stored. Please restart the application and add a password.")
        sleep(3)