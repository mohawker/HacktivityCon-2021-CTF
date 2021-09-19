# Miscellaneous
## Bad Words
### Problem Type: Linux Command Injection 
After connecting into the linux machine, we are in the machine's `/home/user` directory

Some letters and characters were filtered in this linux machine: Unable to input simple commands such as `ls` or `cd`

We noted that padding the commands with "" helped bypass the filter - For example, `l""s` or `c""d`

With this, we are able to navigate through the directories and obtain the flag.

Also, we note that `/bin/sh` was also not filtered out, not sure if this was intended in the challenge.

![](https://i.imgur.com/d23Pcfa.png)

## Shelle
### Problem Type: Linux Command Injection
This was a harder command injection challenge, where almost all special characters were filtered out. After enumeration, the only special characters allowed were: `$, >, (, ), [, ], -`

On top of that, there were limited commands we could use.
![](https://i.imgur.com/VP72PyE.png)

We came across this [fantastic resource](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection) - which showed us that we could use `echo -e` to pass the payload into the terminal in hex. From the challenge documents, we knew that the flag was in the `/opt/` folder. Hence, we crafted a payload (in hex) to `cat /opt/flag.txt`

![](https://i.imgur.com/SHuZPk4.png)

We then obtain the flag. 

## Redlike
### Linux Privlege Escalation
Using Redis
