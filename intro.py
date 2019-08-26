#!/usr/bin/env python3
#
# Script to teach the basics of linux to someone who has never used it before
#
# Author: Scott Brink
#
# www.github.com/sebrink/intro2linux
#

import sys,os,signal
from subprocess import check_output

# Color codes
redStart = "\033[91m"
redEnd = "\033[00m\u001b[0m"
greenStart = "\033[92m"
greenEnd = "\033[01m\u001b[0m"

def gprint(line):
    print(greenStart+line+greenEnd) 

# Catches ctrl+c and exits cleanly.
def signal_handler(sig, frame):
    gprint("\n\nProgram exited. Welcome to linux!")
    sys.exit(0)

def tux():
    gprint("\n         _nnnn_")
    gprint("        dGGGGMMb     ,\"\"\"\"\"\"\"\"\"\"\"\"\"\".")
    gprint("       @p~qp~~qMb    | Linux Rules! |")
    gprint("       M|@||@) M|   _;..............\'")
    gprint("       @,----.JM| -\'")
    gprint("      JS^\__/  qKL")
    gprint("     dZP        qKRb")
    gprint("    dZP          qKKb")
    gprint("   fZP            SMMb")
    gprint("   HZM            MMMM")
    gprint("   FqM            MMMM")
    gprint(" __| \".        |\dS\"qML")
    gprint(" |    `.       | `\' \Zq")
    gprint("_)      \.___.,|     .\'")
    gprint("\____   )MMMMMM|   .\'")
    gprint("     `-'       `--' hjm")

def ls():
    gprint("\nTo exit at any point, type "+redStart+"\"ctrl+c\""+redEnd+greenStart+".\n"+greenEnd)
    gprint("First, let me introduce you to the shell.\n")
    gprint("This is the command line in linux that let's you run commands, it's a very powerful tool.\n")
    gprint("The first command to learn is "+redStart+"\"ls\""+redEnd+greenStart+" which will list the current files within your directory.\n"+greenEnd)
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"ls\""+redEnd+greenStart+" to continiue: "+greenEnd)
        if cmd != "ls":
              gprint("\nType "+redStart+"\"ls\""+redEnd+greenStart+".\n"+greenEnd)
        else:
            print("")
            print(check_output("ls").decode())
            return

def lsla():
    gprint("You can also add arguments to your commands.\n")
    gprint("Try typing "+redStart+"\"ls -la\""+redEnd+".\n"+greenEnd)
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"ls -la\""+redEnd+greenStart+" to continue: "+greenEnd)
        if cmd != "ls -la" and cmd != "ls -al":
           gprint("\nType "+redStart+"\"ls -la\""+redEnd+".\n"+greenEnd)
        else:
            print("")
            print(check_output(["ls", "-la"]).decode())
            gprint("This is using two flags, "+redStart+"-a"+redEnd+greenStart+" and "+greenEnd+redStart+"-l"+redEnd+greenStart+".\n"+greenEnd)
            gprint(redStart+"\"-a\""+redEnd+greenStart+" shows hidden files, while "+redStart+"\"-l\""+redEnd+greenStart+" shows more information about a file in a long listing format.\n"+greenEnd)
            gprint("To read more about these commands, you can type "+redStart+"\"man ls\""+redEnd+greenStart+".\n"+greenEnd) 
            gprint("You can replace the "+redStart+"\"ls\""+redEnd+greenStart+" with the name of any command you want in order to learn more about how to use each command.\n"+greenEnd)
            return

# Combined into one as they are intertwined
def pwd_cd():
    gprint("Now, time to figure out where we are.\n")
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"pwd\""+redEnd+greenStart+": "+greenEnd)
        if cmd != "pwd":
            gprint("\nType "+redStart+"\"pwd\""+redEnd+greenEnd+"\n")
        else:
            print("")
            print(check_output(["pwd"]).decode())
            gprint("This command means print working directory, which prints the directory you are currently working in.\n")
            break

    home = os.environ["HOME"]
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"cd /\""+redEnd+greenStart+": "+greenEnd)
        if cmd != "cd /":
            gprint("\nType "+redStart+"\"cd /\"\n"+redEnd)
        else:
            break

    gprint("\nWe have now gone to the base directory of our operating system. Type "+redStart+"\"pwd\""+redEnd+greenStart+" to see that we are actually there.\n"+greenEnd)
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"pwd\""+redEnd+greenStart+": "+greenEnd)
        if cmd != "pwd":
            gprint("\nType "+redStart+"\"pwd\"\n"+redEnd)
        else:
            # No need to actually move the user, just give the illusion.
            print("\n/\n")
            break

    gprint("And now we want to jump back to our home directory.\n")
    gprint("So we can now type "+redStart+"\"cd\""+redEnd+greenStart+" with no arguments to get to the home directory of the user we are currently logged in as.\n"+greenEnd)
    while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"cd\""+redEnd+greenStart+": "+greenEnd)
        if cmd != "cd":
            gprint("\nType "+redStart+"\"cd\"\n"+redEnd)
        else:
            # No need to actually change the directory, the script will output to wherever it was run.
            gprint("\nCool. We are now back in our home directory.\n")
            return

def cat():
   gprint("Final thing. There is a file on linux with the name of every user who is registered on the machine. It's called \"/etc/passwd\".\n")
   gprint("Let's read that file by using the cat command.\n")
   gprint("Type "+redStart+"\"cat /etc/passwd\"\n"+redEnd)
   while True:
        cmd = input(greenStart+"Enter the command "+redStart+"\"cat /etc/passwd\""+redEnd+greenStart+": "+greenEnd)
        if cmd != "cat /etc/passwd":
            print(greenStart+"\nType "+redStart+"\"cat /etc/passwd\"\n"+redEnd)
        else:
            print(check_output(["cat","/etc/passwd"]).decode())
            return

def done():
    gprint("And with that, we are done. I hope you feel more comfortable on the linux command line!\n")
    cmd = input(greenStart+"Hit any key to leave this script.\n"+greenEnd)
    sys.exit(0)

def main():
    # Used to catch ctrl+c
    signal.signal(signal.SIGINT, signal_handler)
    tux()
    ls()
    lsla()
    pwd_cd()
    cat()
    done()

if __name__ == '__main__':
    main()
