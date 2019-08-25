#!/usr/bin/env python3
#
# Script to teach the basics of linux to someone who has never used it before
#
# Author: Scott Brink
#

import sys,os,signal
from subprocess import check_output

# Catches ctrl+c and exits cleanly.
def signal_handler(sig, frame):
    print('\n\nProgram exited. Welcome to linux!')
    sys.exit(0)

def ls():
    print("\nTo exit at any point, type \"ctrl+c\".\n")
    print("First, let me introduce you to the shell!\n")
    print("This is the command line in linux that let's you run commands, it's a very powerful tool.\n")
    print("The first command to learn is \"ls\", which will list the current files within your directory.\n")
    while True:
        cmd = input("Enter the command \'ls\' to continiue: ")
        if cmd != "ls":
              print("\nType \'ls\'.\n")
        else:
            print("")
            print(check_output("ls").decode())
            return

def lsla():
    print("You can also add arguments to your commands!\n")
    print("Try typing \"ls -la\"\n")
    while True:
        cmd = input("Enter the command \'ls -la\' to continue: ")
        if cmd != "ls -la" and cmd != "ls -al":
           print("\nType \'ls -la\'.\n")
        else:
            print("")
            print(check_output(["ls", "-la"]).decode())
            print("This is using two flags, -a and -l.\n-a shows hidden files, while -l shows more information about a file in a long listing format.")
            print("To read more about these commands, you can type \"man ls\". You can replace the \"ls\" with the name of any command you want in order to learn more about how to use each command!")
            return

# Combined into one as they are intertwined
def pwd_cd():
    print("Now, time to figure out where we are!")
    while True:
        cmd = input("Enter the command \"pwd\": ")
        if cmd != "pwd":
            print("\nType \"pwd\"")
        else:
            print("")
            print(check_output(["pwd"]).decode())
            print("This command means print working directory, which prints the directory you are currently working in.")
            break

    home = os.environ["HOME"]
    print("We are in your home directory now, denoted by \'"+home+"\'")
    while True:
        cmd = input("Enter the command \"cd /\": ")
        if cmd != "cd /":
            print("\nType \"cd /\"")
        else:
            break

    print("\nWe have now gone to the base directory of our virtual machine!  Type pwd to see that we are actually there!")
    while True:
        cmd = input("Enter the command \"pwd\": ")
        if cmd != "pwd":
            print("\nType \"pwd\"")
        else:
            # No need to actually move the user, just give the illusion.
            print("\n/\n")
            break

    print("And now we want to jump back to our home directory, so we can now type \"cd\" with no arguments to get to the home directory of the user we are currently logged in as.")
    while True:
        cmd = input("Enter the command \"cd\": ")
        if cmd != "cd":
            print("\nType \"cd\"")
        else:
            print("\nCool!  We are now back in our home directory!")
            return

def cat():
   print("Final thing! There is a file on linux with the name of every user who is registered on the machine! It's called \"/etc/passwd\"")
   print("Let's read that file by using the cat command!")
   print("Type \"cat /etc/passwd\"\n")
   while True:
        cmd = input("Enter the command \"cat /etc/passwd\": ")
        if cmd != "cat /etc/passwd":
            print("\nType \"cat /etc/passwd\"")
        else:
            print(check_output(["cat","/etc/passwd"]).decode())
            return

def done():
    print("And with that, we are done! I hope you feel more comfortable on the linux command line!")
    sys.exit(0)

def main():
    # Used to catch ctrl+c
    signal.signal(signal.SIGINT, signal_handler)
    ls()
    lsla()
    pwd_cd()
    cat()
    done()

if __name__ == '__main__':
    main()
