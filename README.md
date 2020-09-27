



[![N|Solid](https://insec.in/wp-content/uploads/2020/07/hackthebox.png)](https://nodesource.com/products/nsolid)
# HackTheBox Writeups :
---
+ Writeups built by me which can give you the initial idea of how i successfully owned both user and root of some boxes that i tried to exploit. I do try to put the instructions as detailed and as step-by-step as possible, if there is any confusion, issue it as will.

+ Before reading, i assume you have already known what is HackTheBox and how to run its openvpn pack in order to connect to the targets and exploit them. if not then here...
> Hack The Box is an online platform allowing you to test your penetration testing skills andexchange ideas and methodologies with thousands of people in the security field. Click below to hack our invite challenge, then get started on one of our many live machines or challenges. In order to join it, create an account and join at https://www.hackthebox.eu/login, the login part could be tricky since it will ask you to "hack" your way in, find the invitation code in order to proceed any further, once succeeded, choose a server at the "Access" tab, download the opvnpn pack, run it and you will establish yourself a connection to those boxes, after that, have fun hacking.

- Running the openvpn pack :
```sh
$ cd Downloads # Changing to the directory where the pack is located
$ sudo openvpn hacktheboxpack.ovpn
```
- then you will have access to one of the boxes

<p align="center"><img src="https://github.com/Zenix-Owler/HTB-Writeup/blob/master/ping?raw=true"></p>

- If you still have any problem trying to setup your hackthebox account or its infrastructure, join HackTheBox's discord here https://discord.com/invite/hRXnCFA for more help.

### Structure of my Writeups :
---
  - ##### Requirements
    + Basic knowledge of some kind that you should know first before proceeding.
  - ##### Enumeration
    + Footprinting the target.
  - ##### Privilege Escalation
    + Escalate our current privilege to obtain the user.txt flag.
  - ##### Full Control
    + Rooting the server and obtain the root.txt flag.

### Logs :
---
Logs of each time i commit a new writeup. Its metadata and the commitment date. 
| Writeup | OS | BoxAuthor| Level | Commit-Date |
| ------ | ------ | ------ | ------ | ------ |
|Obscurity|Linux|clubby789|Medium|25/9/2020 |
|Buff|Windows|egotisticalSW|Easy|26/9/2020 |


### Credits :
---
- I do detail the information of each box per writeup : OS, Level, BoxAuthor, ... 
- `Writeups by me : ZenixOwler. `
### License :
---
MIT

---
**Writeups... Hoo**

