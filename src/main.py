from sys import getdefaultencoding
import requests
from bs4 import BeautifulSoup as bs4
from html.parser import HTMLParser
from datetime import date


pageHTML = "" #this is the url of the page to be Used for reference.

#All of the elements for a reference, each will have a assigned function that will asign its value.
dateAccesed = ""
datePublished = ""
author = ""
title = ""
pageURL = ""

#these get the data listed in name, and return it.
def getDatePublished():
    input_ = getUserInput("Enter the date published(year.month.day), if left empty will default to 'n.d': ")
    if input_ == "":
        input_ = "n.d."
    
    return input_

def getDateAccessed():
    todaysDate = date.today()
    todaysDate = todaysDate.strftime("%d.%m.%Y")
    return todaysDate

def getAuthor():
    input_ = getUserInput("Enter the author, if left empty will default to 'n.a.': ")
    if input_ == "":
        input_ = "n.a."

    return input_

def getTitle():
    pass

def getPageURL():
    pass

#Gets the URL using requests and Bs4
def getHTML():
    global pageURL

    input_ = getUserInput("Enter the URL: ")
    pageURL = input_

    page = requests.get(input_)
    soup = bs4(page.text, 'html.parser')

#This method is for obtaining user input from the cli, 
#it takes the text to display to user as a parameter and returns the user input.
#May move to seperate file in future for modularity(?)
def getUserInput(_text): 
    input_ = input(_text)
    return input_

def main(): #this is the main method, it will be called when the program is run.
    getHTML()
main()

