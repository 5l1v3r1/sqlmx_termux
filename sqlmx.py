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
   print("\u001b[33m[*] SELECT A CODE TO INJECTION")
   print(" ")
   print("\u001b[0m[1] index.php?id=")
   print("[2] files.php?id=")
   print("[3] shop.php?id=")
   print("[4] buy.php?category=")
   print("[5] trainers.php?id=")
   print("[6] games.php?id=")
   print("[7] page.php?file=")
   print("[8] gallery.php?id=")
   print("[9] show.php?id=")
   print(" ")
   inject=int(input("SELECT YOUR CODE: "))
   print("\u001b[31m///////////////////////////////////")
   print("\u001b[32m ")
   print("[*] INJECTING CODE...")
   os.system('sleep 2')
   print(" ")
   print("\u001b[0m[*] IF YOU SEE A SQL SYNTAX ERROR")
   os.system('sleep 1')
   print("[*] THAT NOTICES YOU A VULNERABILITY")
   os.system('sleep 2')
   if(inject==1):
     try:
         inject="/index.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==2):
     try:
         inject="/files.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==3):
     try:
         inject="/shop.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==4):
     try:
         inject="/buy.php?category='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==5):
     try:
         inject="/trainers.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==6):
     try:
         inject="/games.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==7):
     try:
         inject="/page.php?file='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==8):
     try:
         inject="/gallery.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   elif(inject==9):
     try:
         inject="/show.php?id='"
         webbrowser.open((target+inject))
     except KeyboardInterrupt:
         screen()
         select()
   else:
     print("\u001b[31m[*] WRONG OPTION...")
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
     dorks()
   elif(choose==0):
     update()
   else:
     print("\u001b[31m[*] WRONG OPTION...")
#DORK SELECTING...
def dorks():
   print("\u001b[31m///////////////////////////////////")
   print("\u001b[0m[1] index.php?id=")
   print("[2] files.php?id=")
   print("[3] shop.php?id=")
   print("[4] buy.php?category=")
   print("[5] trainers.php?id=")
   print("[6] games.php?id=")
   print("[7] page.php?file=")
   print("[8] gallery.php?id=")
   print("[9] show.php?id=")
   print(" ")
   dorking=int(input("SELECT YOUR DORK: "))
   print("\u001b[31m///////////////////////////////////")
   if(dorking==1):
     try:
         url='https://www.google.com/search?q=index.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==2):
     try:
         url='https://www.google.com/search?q=files.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==3):
     try:
         url='https://www.google.com/search?q=shop.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==4):
     try:
         url='https://www.google.com/search?q=buy.php?category='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==5):
     try:
         url='https://www.google.com/search?q=trainers.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==6):
     try:
         url='https://www.google.com/search?q=games.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==7):
     try:
         url='https://www.google.com/search?q=page.php?file='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==8):
     try:
         url='https://www.google.com/search?q=gallery.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   elif(dorking==9):
     try:
         url='https://www.google.com/search?q=show.php?id='
         webbrowser.open(url)
     except KeyboardInterrupt:
         screen()
         select()
   else:
     print("\u001b[31m[*] WRONG OPTION...")
#WHOLE PROGRAM IN HERE...
try:
    screen()
    select()
except KeyboardInterrupt:
    print("[*] GOODBYE...")