from sys import getdefaultencoding
import webbrowser
import requests
from bs4 import BeautifulSoup as bs4
from html.parser import HTMLParser
from datetime import date
import website

running = True
ref = ""

def helpCommand():
    print("\n\nhelp - displays this message")
    print("exit - exits the program")
    print("getweb - gets the data from a webpage")
    print("getbook - gets the data from a book(not implemented)")
    print("license - displays the license(not implemented)")
    print("version - displays the version(not implemented)\n\n")
def exitCommand():
    running = False
    exit()
def getWebCommand():
    ref = website.getReferanceWeb()
    print(ref)
def getBookCommand():
    pass
def licenseCommand():
    pass
def versionCommand():
    pass



def main(): #this is the main method, it will be called when the program is run.
     
    while True:
        getCommand()

def getCommand():
    input_ = input("Enter command(help for list of commands): ")
    if input_ == "help":
        helpCommand()
    elif input_ == "exit":
        exitCommand()
    elif input_ == "getweb":
        getWebCommand()
        
    elif input_ == "getbook":
        getBookCommand()
    elif input_ == "license":
        licenseCommand()
    elif input_ == "version":
        versionCommand()
    else:
        print("Invalid command: " + input_ + " (Try " + "\"help\"" + " for a list of commands)")

    


        


main()

