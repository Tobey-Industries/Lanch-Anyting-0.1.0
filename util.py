import os
os.system("cls")
print("Starting Log-in Manager...")
usrprofile = os.environ['USERPROFILE']
os.system("cls")
print("""
Percentage Bar: █ 
Description: Importing Libraries and Neccessary functions
""")
from playsound import playsound
from cryptography.fernet import Fernet
import socket
import platform
import time
import psutil
from tkinter import *
def env(var):
  try:
    vari = os.environ[var]
    return vari
  except OSError: error("OSError","env()")
osutildir = env("APPDATA")+"\\..\\LocalLow\\osutil"
logfile = f"{osutildir}\\{socket.gethostname()}.txt"
logpl = logfile
clock = time.strftime('%B-%d-%Y %I:%M %p')


def error(desc, function):
  log(logpl, f"\n--Potted error--\nDescription: {desc}\nFunction: {function}\n")
  ws = Tk()
  ws.config(background="white")
  ws.title('Attention')
  img = PhotoImage(file=osutildir+"\\Error.png")
  Label(ws, image=img).pack(side = LEFT)
  Label(ws, text="The command done an illegal operation and was shut down.\nReinstalling this feature may help.", font="Cascadia 10", foreground="red", background="white").pack(side = RIGHT)
  Button(ws, text="OK",command=ws.destroy, font="Cascadia 5").pack(side=BOTTOM)
  root = ws
  root.geometry("1024x768")
  scrollbar = Scrollbar(root)
 
  scrollbar.pack( side = RIGHT, fill = Y )
  
  mylist = Listbox(root, yscrollcommand = scrollbar.set, width=70)
  mylist.insert(END, 'Debug Info: ')
  mylist.insert(END, 'Device: '+socket.gethostname())
  mylist.insert(END, 'Device IP: '+socket.gethostbyname(socket.gethostname()))
  mylist.insert(END, 'Kernel: '+os.name)
  mylist.insert(END, 'Function: '+function)
  mylist.insert(END, 'Error Description: '+desc)
  mylist.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = mylist.yview )
  ws.mainloop()
def log(logfile, info):
  try:
    with open(logfile, "a")as f: f.write("\n"+clock+"|"+info)
  except UnicodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(clock, encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except UnicodeEncodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(clock, encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except FileNotFoundError: 
    print("--LogFile Error--\nThe system cannot find the path specified.")
    error("FileNotFoundError", "log()")

time.sleep(0.90)
os.system("cls")
print("""
Percentage Bar: █ █
Description: Defining Variables
""")


osn = os.environ ['OS']
windir = os.environ ['WINDIR']
processor = os.environ['PROCESSOR_IDENTIFIER']
architecture = os.environ['PROCESSOR_ARCHITECTURE']
processors = os.environ['NUMBER_OF_PROCESSORS']
allsyspaths = os.environ['Path']
sysusrname = os.environ['USERNAME']
kernbuild = "UTIL Kernel 0.2.0(2023 Kernel)"
copyright = "Copyright(c) Tobey Enterprises"
pythoncopyright = "Copyright(c) Python Software Foundation"
mscopyright = "Copyright(c) Microsoft Corporation 2006-2023"
ntfourlogonsoundcopyright = "Copyright(c) Microsoft Corporation"

batteryf = psutil.sensors_battery()
battery = batteryf.percent if batteryf else 0
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

userprofile = os.environ ['USERPROFILE']
date = clock
all_info = [sysusrname + "|" + date + "|" + hostName + '|' + hostIP + " " + userprofile + "|" + osn + "|" + windir + "|" + processor + "|" +  architecture + "|" + processors]
shellbuild = "Launch Anything 1.1.0(2023-March Shell)"
help = """
Commands:
[1] Run Windows Files
[2] Run Python3 Files on Bash
[3] Run Python2 Files on Bash
[4] Run Python2 or Python3 Files on Windows New Technology
[9] Install PIP-Pyinstaller
[10] Install PIP-Python3 on Bash
[11] Run Pyinstaller
[12] Update PIP
[13] Run Command Prompt
[14] Set Color
[15] Set Color Code
[16] Set Title of the Running Windows Command Processor
[17] Run Notepad
[18] Run Windows Explorer
[19] Run Write
[20] Run WINVER
[21] Run REGEDIT
[22] Run Task Manager
[23] Kill any process
[24] Diagnose websites
[25] Go to websites
[26] Hack websites
[27] Clear Screen
[28] Run Dreamco
[29] Go to youtube.com
[30] Go to bing.com
[31] Display all System Info
[32] Display all the current directory neatly
[33] Play a sound
[34] Log the system environment variables
[35] About Launch Anything 0.1.0-1.1.0
[36] About Utility Kernel 0.2.0-1.0.0
[37] Operating System Version
[Ctrl+Z] Exit Launch Anything
"""
primos = "nt"
oscheck = True
debugsys = True
nocolor = False
sysusersinfo = f"{osutildir}\\sysUsers.txt" 
tiny_info = [battery, osn, architecture, hostName]
unattended = False
cmdlist = ["--no-sys-check", "--primary-os-linux", "--fileopen", "--display-date"]
os.system(f"title {kernbuild}:{shellbuild}")
time.sleep(0.90)
os.system("cls")
print("""
Percentage Bar: █ █ █ 
Description: Defining Functions and behaviors
""")  
def uac(func, ticket, forced):
            global status


            def button_command_right_without_password():


                status = True
                os.system("pause")
            def button_command_wrong():

                global status
                status = False
                os.system("pause")
            def button_command_right_with_password():
                      global status
                      key = "your key"
                      fernet = Fernet(key)
                      fil = open(current_user_dir+"\\pass.txt", "rb")
                      passenc = fil.read()
                      dcrpswd=fernet.decrypt(passenc)
                      inps = input("Password to Authorize: ")
                      rpswdo = str(dcrpswd)
                      rpswd = rpswdo[2:int(len(rpswdo))-1]
                      global status
                      def button_command():
                          global status
                          if inps == rpswd:
                            key = "Access is denied."
                            status = True
                            os.system("pause")
                          else:
                            print("Not Accepted")
                            key = "Access is denied."
                            status = False
                            os.system("pause")
                          
                      
            print(f"Do you want this function to make security changes?\nPublisher info: {ticket}\nFunction Name: {func}")
            if forced == False:
              opt = input("Y/N: ")
              if opt == "Y": button_command_right_without_password()
              elif opt == "y": button_command_right_without_password()
              else: button_command_wrong()   
            else:
              opt = input("Y/N: ")
              if opt == "Y": button_command_right_with_password()
              elif opt == "y": button_command_right_with_password()
              else: button_command_wrong() 

def do(): 
  time.sleep(float(0.40))
def filecontents(filename):
  try:
    op = open(filename)
    return op.read()
  except PermissionError: 
    os.system("cls")
    error("PermissionError", "filecontents()")
  except FileNotFoundError:
    os.system("cls")
    error("FileNotFoundError", "filecontents()")     
def getsysinfo(currtell):
  try:
    user = os.environ["USERNAME"]
    tmpdir = os.environ["TMP"]
    homedrv = os.environ["HOMEDRIVE"]
    cpucores= os.environ["NUMBER_OF_PROCESSORS"]
    cpugen = os.environ["PROCESSOR_LEVEL"]
    root = os.environ["SystemRoot"]
    ops = platform.system()
    arc = os.environ["PROCESSOR_ARCHITECTURE"]
    info = f"""
A = Object       B = Meaning                                      C = Information from                                         
-------------  --------------------------------------------  ----------------
[A]HostName     = [B]{socket.gethostname()}                      = [C]Socket Library
[A]HostIP       = [B]{socket.gethostbyname(socket.gethostname())}= [C]Socket Library
[A]Operating
System          = [B]{ops}                                       = [C]{os.name}OSKRNL
[A]{ops}
User            = [B]{user}                                      = [C]{os.name}OSKRNL
[A]Kernel Build = [B]{kernbuild}                                     = [C]UTILITY Kernel
[A]OS Kernel    = [B]{os.name}                                   = [C]{os.name}OSKRNL
[A]Copyright    = [B]{copyright}                                 = [C]UTILITY Kernel
[A]Temporary Dir= [B]{tmpdir}                                    = [C]{os.name}OSKRNL
[A]HomeDrive    = [B]{homedrv}                                   = [C]{os.name}OSKRNL
[A]Root User's
Directory       = [B]{root}                                      = [C]{os.name}OSKRNL
[A]CPU Cores    = [B]{cpucores}                                  = [C]{os.name}OSKRNL
[A]CPU Level    = [B]{cpugen}                                    = [C]{os.name}OSKRNL
[A]CPU 
Architecture    = [B]{arc}/AMD64(An Interpreting Flaw in 32-bit) = [C]{os.name}OSKRNL
-----------------------------------------------------------------------------
Caller: {currtell}
  """
    return info
  except OSError: 
    os.system("cls")
    error("OSError", "getsysinfo()")
def writeBINARY(bin, file):
  os.system(f'echo "">"{file}"')
  with open(file, "wb")as f: f.write(bin)
def writeASCII(cont, file):
  os.system(f'echo "">"{file}"')
  with open(file, "w")as f: f.write(cont) 
time.sleep(0.9)
os.system("cls")
print("""
Percentage Bar: █ █ █ █ 
Description: Successfully done the important configurations + running the bootsound + running the user manager
""")
fsound = filecontents(osutildir + "\\bootsound.sys")
setsound = fsound
secsound = filecontents(osutildir + "\\secbootsound.sys")
try: playsound(setsound)
except TypeError: playsound(secsound)
time.sleep(0.9)
os.system("cls")
try:
  usrs = filecontents(sysusersinfo)
  print("Users: " + usrs)
except: print("The returning value wasn't made.")
while True:
  current_user = input("Username: ")
  if current_user == "null" or current_user == "":
    print("None is not allowed")
    current_user = input("Username: ")
  current_user_dir = osutildir+"\\"+current_user
  
  if current_user == "Guest":
    print("Welcome Guest!")
    current_user_dir = env("PUBLIC")
    break
  else:
    try:
      open(current_user_dir+"\\sysUser.txt")
      key = 'your key'
      fernet = Fernet(key)
      fil = open(current_user_dir+"\\pass.txt", "rb")
      passenc = fil.read()
      dcrpswd=fernet.decrypt(passenc)
      inps = input("Password: ")
      rpswdo = str(dcrpswd)
      rpswd = rpswdo[2:int(len(rpswdo))-1]
      if inps == rpswd:
        print(f"Welcome {current_user}!")
        log(logpl, current_user_dir)
        key = "Access is denied."
        break
      else:
        print("Invalid Passcode!")
    except FileNotFoundError: print("Invalid User")
    except TypeError: error("TypeError", "password manager")
    except UnicodeError: print("Numbers+Letters are the only elements supported.")
    except EOFError: print("CTRL+Z/CMD+X/CMD+Z are illegal operations.")
    except NameError: error("NameError", "password manager")
print("""
Percentage Bar: █ █ █ █ █ Done! 
Description: Running the autorun manager + configuring the system + running Charms Window 
""")
try: 
  import time
  loc = open("config.util")
  fin = loc.read()
  if fin == "--no-sys-check":
    oscheck = False
    time.sleep(int(10))
  elif fin == "--primary-os-linux":
    primos = "posix"
    time.sleep(int(10))
  elif fin == "--fileopen":
    run = input("Run:")
    try: os.startfile(run)
    except FileNotFoundError:
      print("Invalid File")
      log(logpl, f" FileNotFoundError. When opening: {run}. Using: StartRun")
    except OSError:
      print("Invalid File Content")
      print("Invalid Content")
      log(logpl, f" OSError. When opening: {run}. Using: StartRun")
      logp = open(logpl)       
    time.sleep(int(10))
  elif fin == "--display-date":
    import time
    print(time.strftime("%m-%d-%y"))
    time.sleep(int(10))
  elif fin == "--no-color": nocolor = True
  elif fin == "--no-spec": debugsys = False  
  else: unattended = True  
  loc.close() 

except NameError:
  print("X")
except FileNotFoundError:
  print("X")
except TypeError: error("TypeError","autorun")
except UnicodeError: print("Numbers+Letters are the only elements supported.")
except EOFError: print("CTRL/CMD-Z & CTRL/CMD-X are illegal operations.")
try: os.startfile("charms.exe")
except: os.startfile("charmswindow.pyw")
writeASCII(help, usrprofile + "\\AppData\\Roaming\\help.txt")
writeASCII(open(logpl).read(), usrprofile + "\\AppData\\Roaming\\dbginfo.txt")
if nocolor: os.system("color")
else: os.system("color B0")
if oscheck:
  if os.name == primos:
    print(f"*{primos}")
  else:
    import time
    print("Operating System Not Supported!")
    time.sleep(int(15))
    print("Exiting...")
    time.sleep(int(20))
    exit()
time.sleep(0.9)
os.system("cls")
print("Successfully started! Debug info: ")
if debugsys:
  print(platform.system(), os.name)
  print(date)
  print(hostName)
  print(hostIP)
  print(battery)

print("System Started... Done")
log(logpl, " System Started Successfully at "+date)
time.sleep(0.9)
os.system("cls")
os.system("ver")
print("""Options:
[1] Run Windows Files
[4] Run Python2 or Python3 Files on Windows New Technology
[9] Install PIP-Pyinstaller
[11] Run Pyinstaller
[12] Update PIP
[13] Run Command Prompt
[14] Set Color
[15] Set Color Code
[16] Set Title of the Running Windows Command Processor
[17] Run Notepad
[18] Run Windows Explorer
[19] Run Write
[20] Run WINVER
[21] Run REGEDIT
[22] Run Task Manager
[23] Kill any process
[24] Diagnose websites
[25] Go to websites
[26] Hack websites
[27] Clear Screen
[28] Run Dreamco
[29] Go to youtube.com
[30] Go to bing.com
[31] Display all System Info
[32] Display all the current directory neatly
[33] Play a sound
[34] Log the system environment variables
[35] About Launch Anything 0.1.0-1.1.0
[36] About Utility Kernel 0.2.0-1.0.0
[37] Operating System Version
[Ctrl+Z] Exit Launch Anything
""")   
while True:
  try:
        if unattended:
            opt = open("config.util").read()
            unattended = False
        else: opt = input(f"{current_user}@{hostName}: ")
        log(logfile, f" {sysusrname} {current_user_dir} Ran option: {opt}")
        if opt == "27": os.system("cls")
        elif opt == "36": print("Utility Kernel 0.2.0-1.0.0\nCopyright (C) TE 2023")
        elif opt == "37": os.system("ver")
 
        elif opt == "33":
          sound = input("File or Website: ")
          if sound[0] == '"' and sound[int(len(sound))-1] == '"': sound = sound[1:int(len(sound))-1]
          else: sound = sound
          playsound(sound)
        elif opt == "34": 
          inf = getsysinfo(current_user)
          log(logpl, inf)
        elif opt == "35":
          import tkinter
          window = tkinter.Tk()
          tkinter.Label(window,text = "Copyight (C) Tobey Enterprises\n Copyright (C) Tobey Industries\n 2022-2023").pack()
          tkinter.Label(window,text="Shell Version: "+shellbuild).pack()
          tkinter.Label(window,text="Kernel Version: "+kernbuild).pack()
          tkinter.Label(window,text="Success Sound Copyright: "+ntfourlogonsoundcopyright).pack()
          tkinter.Label(window,text="Main OS Copyright: "+mscopyright).pack()
          tkinter.Label(window,text="Code Copyright: "+copyright).pack()
          tkinter.Button(window,text="OK", command = window.destroy).pack()
          window.title("About Launch Anything")
          window.geometry("400x400")
          window.mainloop()
        elif opt == "32": os.system("dir /w")  
        elif opt == "31": print(all_info)          
        elif opt == "1": 
                try:
                  run = input("Run: ")
                  os.startfile(run)
                except FileNotFoundError:
                  print("Invalid File!")
                except OSError:
                  print("Invalid win32 user mode executable!")
        elif opt == "print(tiny_info)": print(tiny_info)
        elif opt == "print(all_info)": print(all_info)
        elif opt == "print(osn)": print(osn)
        elif opt == "print(hostIP)": print(hostIP)
        elif opt == "do()": do()
        elif opt == "os": print(os)
        elif opt == "print(battery)": print(battery)
        elif opt == "winver": opt = "winver"
        elif opt == "29":
          import webbrowser
          webbrowser.open("youtube.com")
        elif opt == "30":
          import webbrowser
          webbrowser.open("bing.com")      
        elif opt == "28":
                dot = 0
                while dot < 9:
                  dot = dot + 1
                  os.system("cls")
                  os.system("color 00")
                  do()
                  os.system("color 10")
                  do()
                  os.system("color 20")
                  do()
                  os.system("color 30")
                  do()
                  os.system("color 40")
                  do()
                  os.system("color 50")
                  do()
                  os.system("color 60")
                  do()
                  os.system("color 70")
                  do()
                  os.system("color 80")
                  do()
                  os.system("color 90")
                  do()
                  os.system("color A0")
                  do()
                  os.system("color B0")
                  do()
                  os.system("color C0")
                  do()
                  os.system("color D0")
                  do()
                  os.system("color E0")
                  do()
                  os.system("color F0")
                  do()
                  os.system("color B0")
        elif opt == "2": os.system("python3 " + input("File: "))
        elif opt == "3": os.system("python " + input("File: "))
        elif opt == "4": os.system("python " + input("File: "))      
        elif opt == "9":
                os.system("pip install pyinstaller")
                os.system("color 10")
        elif opt == "14":
                out = input("""
0 = Black       8 = Gray
1 = Blue        9 = Light Blue
2 = Green       A = Light Green
3 = Aqua        B = Light Aqua
4 = Red         C = Light Red
5 = Purple      D = Light Purple
6 = Yellow      E = Light Yellow
7 = White       F = Bright White
                """)
                os.system("color " + out + "0")
        elif opt == "24":
                ping = input("Website: ")
                os.system("ping " + ping)
        elif opt == "25":
                import webbrowser
                web = input("Go to: ")
                webbrowser.open(web)
        elif opt == "26":
                print("""
██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                """)
                try:
                  import requests
                  ip = input("Enter IP To Scan: ")
                  url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
                  response = requests.get(url).json
                  print("IP: " + ip)
                  print("\n")
                  print("ADDRESS:")
                  print("Country Code:", response['country'])
                  print("Region Name:", response['region'])
                  print("City:", response['city'])
                  print("\n")
                  print("POSTAL/TIMEZONE:")
                  print("Postal Code:", response['postal'])
                  print("Timezone:", response['timezone'])
                  print("\n")
                  print("LAT/LONG")
                  print("Location:", response['loc'])
                  log(logpl, f" IP: (ip) Location: {response['loc']} Country: {response['country']} Postal Code: {response['postal']}")
                except KeyError:
                  print("Invalid IP Address")
                  log(logpl,f" KeyError (Invalid IP Address) Using IP-Pirate |{date} {hostIP} {userprofile} {current_user} {os.name}")                  
                except ImportError:
                  print("A dll or python pip file is corrupted!")
                  log(logpl, f" ImportError Using IP-Pirate |{date} {hostIP} {userprofile} {current_user} {os.name}")
                except TypeError:
                  print("Python Build Is too old! or A .dll file is corrupted")
                  log(logpl, all_info + " Corrupted System")
        elif opt == "13":
                os.system("cmd")
        elif opt == "16":
                tit = input("Title: ")
                os.system("title " + tit)
        elif opt == "15":
                coc = input("Color: ")
                os.system("color " + coc)
        elif opt == "17":
                filnam = input("New File: ")
                os.system(f"notepad {filnam}")
        elif opt == "18":
                os.system(f"explorer {current_user_dir}")
        elif opt == "19":
                os.startfile("write")
        elif opt == "20":
                os.startfile("winver")
        elif opt == "21":
                os.startfile("REGEDIT")
        elif opt == "22":
                os.startfile("taskmgr")
        else: os.system(opt)
  except EOFError:
    log(logpl, " Shutdown (expected)")
    print("Shutting Down...")
    os.system("del config.util")
    os.system("cls")
    do()
    exit()
  except TypeError: print("An error occurred.(TypeError)")
 
  except UnicodeError: print("An error occurred.(UnicodeError)")
  except KeyboardInterrupt: print("An error occurred.(KeyboardInterrupt)")
  except FileNotFoundError: print("An error occurred.(FileNotFoundError)")
  except OSError: print("An error occurred.(OSError)")
  except PermissionError: print("An error occurred.(PermissionError)")
