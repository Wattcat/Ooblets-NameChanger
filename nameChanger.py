# Script changes the name of a charachter in Ooblets
# Please back up your files before running this program
import os
import re


# playerName
path = os.getenv('APPDATA')
path = str(path).replace("Roaming", r"LocalLow\Glumberland\ooblets\SaveData")

saves = os.listdir(path)


# Method keeps track on users in a dictionary
# Assigns name to its foldername
def getNames():
    allnames = {}
    for i in saves:
        gamefile = [f for f in os.listdir(path+"\\"+i)]
        # Takes the first file and checks the name
        filepath = path+"\\"+i+"\\"+gamefile[0]
        f = open(filepath, "r", encoding='utf-8')
        data = f.read()
        # finds startindex of names
        playerPosition = [m.start() for m in re.finditer('playerName', data)]
        # This grabs the enire name, if name is longer than 50 it will not work
        playername = data[playerPosition[1]:playerPosition[1]+50]
        playername = playername[playername.find(":")+1:playername.find(",")]
        playername = playername.replace(r'"', "")
        allnames[playername] = i

    return allnames


# Method changes the name of the user character
def nameChanger(gamefolder, oldname, newname):
    try:
        files = [f for f in os.listdir(path+"\\"+gamefolder)]
        for i in files:
            # This filepath is the entire "1.sav" type files
            filepath = path+"\\"+gamefolder+"\\"+i
            f = open(filepath, "r")
            data = f.read()
            # Replace the target string
            data = data.replace(oldname, newname)

            # Write the file out again
            with open(filepath, 'w') as file:
                file.write(data)
        return "Sav files have sucessfully been changed"
    except IOError:
        return "Error: File does not appear to exist."


# Method changes the name in the table of contents
def tocChanger(oldname, newname):
    try:
        tocpath = os.getenv('APPDATA')
        tocpath = str(tocpath).replace(
            "Roaming", r"LocalLow\Glumberland\ooblets\ooblets_toc.sav")
        f = open(tocpath, "r", encoding='utf-8')
        data = f.read()
        data = data.replace(oldname, newname)

        # Write the file out again
        with open(tocpath, 'w') as file:
            file.write(data)
        return "ooblets_toc.sav have sucessfully been changed"
    except IOError:
        return "Error: File does not appear to exist."


# This is the main run function
def run():
    print("Found saves:", list(getNames()))
    oldname = input("Please enter the name of the save you want to change:\n")
    nameFromDict = getNames().get(oldname)

    choice = input("Enter yes to confirm: ").lower().strip()
    if choice == "yes" or choice == "y":
        newname = input("Please input your new name: ")
        try:
            print(tocChanger(oldname, newname))
            print(nameChanger(nameFromDict, oldname, newname))
        except:
            print("My program seems to broken :(")
    elif choice.strip().lower == "no" or choice.strip().lower == "n":
        print("goodbye")
    else:
        run()


run()
