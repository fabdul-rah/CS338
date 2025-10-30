# Feraidon AbdulRahimzai
## CS338 - Computer Security
### Reverse Shell Assignment - 10/29/25



# Part 1: Installing a PHP Web Shell


#### a: 
- The way we can execute this linux command is by first uploading our shell written php into the website and then using the command ?command=whoami after the directory of uploadedimages/ along with the file we uploaded. In this case its: 

http://danger.jeffondich.com/uploadedimages/abdulf-webshell1.php?command=whoami

The results of this is:

www-data

#### b.

- The <pre> tag displays the output of system commands with its original formatting.



# Part 2: Looking Around

#### a: 

Danger's website is located in the /var/www/danger.jeffondich.com/uploadedimages and we get to this by using the command: pwd (previous working directory)


#### b: 

Below is the full output i got.

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:102:105::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:103:106:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
syslog:x:104:111::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:112:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:113::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:114::/nonexistent:/usr/sbin/nologin
usbmux:x:109:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
landscape:x:112:116::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:113:117:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
jeff:x:1000:1000:Jeff Ondich,,,:/home/jeff:/bin/bash
postgres:x:114:119:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
bullwinkle:x:1001:1001:Bullwinkle J. Moose,,,:/home/bullwinkle:/bin/bash
dhcpcd:x:115:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
polkitd:x:999:999:User for polkitd:/:/usr/sbin/nologin


I got this information from: "https://www.strongdm.com/blog/how-to-list-users-linux",
the command getent passwd allowed me to get this printout.

#### c. 

I can't open the passwd file. The browser says "This site can't be reached" and says something about the firewall. But it contains the same stuff I was able to get with getent 

#### d. 

No, we don't have access to /etc/shadow and I think it has the passwords for the users that were outputted from the getent passwd command, they should be encrypted as well.

#### e.

Found the hi_jeff.txt "lazuli was here :) imagelist2.php is still up and usable", kindasecret.txt with the frog ascii, supersecret.txt with the moose ascii, moresectrets.txt, .even-more-secrets.txt, youfoundme.txt 

I found all of these by using the find command to look for all directories and files with the secret key word: command = find / -name "*secret*"



# Part 4: Launching a Reverse Shell


#### a.

I found my Kali VM IP address by executing the command ip a. 
eth0 inet 192.168.64.2 


#### b. 

I found the ip addr by commanding "ifconfig" and I found that 192.168.64.1 was my local ip. I would use this IP address because it is direct and a subnet of the IP address.

#### e. 

Yes, I do have a shell now and I can execute commands. I used the hostname command and it returned "kali"


#### f. 

The percents are used as encoding for things/signs such as spaces, double quotes, greater than sign and the ampersand that won't otherwise be understood by the url.

%20: Space ( )

%22: Double quote (")

%3E: Greater-than sign (>)

%26: Ampersand (&)

#### g. 

- Your host machine starts netcat in listen mode on a specific port (6000). It's passively waiting for any machine to connect to it on that port.

- On the Kali VM, we trigger the webshell with a command that tells a bash shell on Kali to initiate an outgoing TCP connection back to your attacker's IP and port (6000). This is the "reverse" part – the target connects to the attacker.

- Once the Kali VM connects to our netcat listener, netcat effectively "hands over" the connection to our terminal. Now, anything we type into that netcat terminal (our host OS) is sent to the bash process on Kali, and Kali's bash output is sent back to our netcat terminal. We now have an interactive shell on the Kali VM, controlled from our host.









