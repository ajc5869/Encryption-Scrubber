#Author: Andrew Cozzetta
#Purpose: Traverse through Google Drive to find non-encrypted, Thumbs.db, .DS_Store, and desktop.ini files
#Last Updated: 7/26/16

import os
import platform
import getpass

def main():
    total_files = 0
    not_encrypted = 0
    thumb_files = 0
    DS_Store_files = 0
    desktop_ini_files = 0

    #Arrays that hold file names discovered per type
    not_encrypted_array = []
    thumb_files_array = []
    DS_Store_files_array = []
    desktop_ini_array = []

    #Determines the platform that the script is currently running on
    #"Windows" -> Running Microsoft Windows
    #"Darwin" -> Running Mac OS X
    #"Linux" -> Running a Linux distribution

    #Clear the command prompt/terminal
    os.system('cls' if platform.system() == "Windows" else "clear")

    #Prints which platform the script is running on
    print("Running on the",platform.system(),"platform")

    #Gets the current users Username
    my_username = getpass.getuser()

    #Determines which directory structure to use
    if platform.system() == "Darwin":
        directory = '/Volumes/Macintosh HD/Users/' + my_username + '/Google Drive'
        print("Google Drive Directory: " + directory)
    if platform.system() == "Windows":
        directory = 'C:\\Users\\' + my_username + '\\Google Drive'
        print("Google Drive Directory: " + directory)
    if platform.system() == "Linux":
        directory = '/home/andrew/Drive'

    #Iterate through the directory to find non-encrypted, Thumbs.db, .DS_Store, and desktop.ini files
    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            if not file.endswith(".bc") and not file.endswith(".bch"):
                not_encrypted_array.append(os.path.join(root, file))
                not_encrypted += 1
            if file == "Thumbs.db.bc" or file == "Thumbs.db" or file == "~$$Thumbs.db.bc":
                thumb_files_array.append(os.path.join(root, file))
                os.remove(os.path.join(root, file))
                thumb_files += 1
            if file == ".DS_Store.bc" or file == ".DS_Store" or file == "~$$.DS_Store.bc":
                DS_Store_files_array.append(os.path.join(root, file))
                os.remove(os.path.join(root, file))
                DS_Store_files += 1
            if file == "desktop.ini" or file == "desktop.ini.bc":
            	desktop_ini_array.append(os.path.join(root, file))
            	#os.remove(os.path.join(root, file))
            	desktop_ini_files += 1

    #Prints the number of non-encrypted files found / total files
    print("\n")
    print(not_encrypted,"/",total_files,"file(s) are not encrypted\n")
    print ("\n".join(not_encrypted_array))
    print("\n")

    #Prints the number of Thumbs.db files found
    print(thumb_files,"Thumbs.db file(s) were found and removed")
    print ("\n".join(thumb_files_array))
    print("\n")

    ##Prints the number of .DS_Store files found
    print(DS_Store_files,".DS_Store file(s) were found and removed")
    print ("\n".join(DS_Store_files_array))
    print("\n")

    ##Prints the number of desktop.ini files found
    print(desktop_ini_files,"desktop.ini file(s) were found")
    print ("\n".join(desktop_ini_array))
    print("\n")
    
main()
