import webbrowser
import os
import threading
from webParserSelenium import *
from csvImport import *
from ip import showIp
import customtkinter as ctk
from tkinter import filedialog

def openFolderBtn():
    folder = os.path.dirname(os.path.abspath(__file__))
    os.startfile(folder)
    print("folder is opened.")

def githubProfileBtn():
    webbrowser.open('https://github.com/OleksandrShenhera1')
    print("GitHub opened.")

isParsing = False

def parseCheck():
    global isParsing
    if isParsing == True:
        return

    isParsing = True
    threading.Thread(target=parseStart, daemon=True).start()

resultDict = None

def parseStart():
    global isParsing
    try:
        global resultDict
        resultDict = parser()
    finally:
        isParsing = False


def saveFile():
    global isParsing
    if isParsing == True:
        return
    global resultDict
    if not resultDict:
        print("(Error) Try to parse films before using save.")
        return
    fileName = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    threading.Thread(target=csvImporter(resultDict, fileName), daemon=True).start


def currentIp():
    global isParsing
    if isParsing == True:
        return
    showIp()    
