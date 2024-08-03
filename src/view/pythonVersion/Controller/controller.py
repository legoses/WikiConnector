# Will hopefully be the interface between the model and the python
import os
import subprocess
#import pandas as pd
import csv
class Controller:
    def __init__(self):
        
        self.currentConnect = 'Wiki'
        self.possibleConnectors = {'Wiki','WorldBank','AppleMusic'}

    def setConnector(self,connector):
        self.currentConnect = connector

    def getConnector(self):
        return self.currentConnect

    def query(self,query):
        text = query
        #print(":",text)
        #path = os.path.abspath(os.getcwd())+"/pythonVersion"
        os.chdir('../') 
        os.chdir('../')
        #os.chdir('../')
        path = os.listdir()
        p2 = os.path.abspath(os.getcwd())
        model = p2+"/model"
        view = p2+"/view"
        #p = os.path.abspath(os.getcwd())+"/view"
        os.chdir(model)
        path2 = os.listdir()
        #print("Files: ",path2)
        #print("Path: ",p2)
        #os.system("python3 WikiSource.py Mike")
        #subprocess.call("python3 WikiSource.py Mike")
        if self.currentConnect == 'Wiki':
            os.system("python3 WikiSource.py "+text+"; mv test.csv "+view+"/pythonVersion")
        elif self.currentConnect == 'WorldBank':
            os.system("python3 WorldBankSource.py "+text+"; mv test.csv "+view+"/pythonVersion")
        elif self.currentConnect == 'AppleMusic':
            os.system("python3 AppleMusic.py "+text+"; mv test.csv "+view+"/pythonVersion")
        os.chdir("../")
        #os.chdir('../')
        os.chdir("view/pythonVersion")
        #print("The dir",os.listdir())
