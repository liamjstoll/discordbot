
import os
import re
import random
import discord
import pandas as pd
import numpy as np
import praw
from praw.models import MoreComments
import openpyxl
from datetime import date
from yahoo_fin import stock_info as si
from yahoo_fin import options as oi
import requests
import sqlite3




# changes "7.45B" to 7450000000.0
def removeMBT(s):
    for i in s:
        if i == 'M':
            return float(s[0:-1])*1000000
        if i == 'B':
            return float(s[0:-1])*1000000000
        if i == 'T':
            return float(s[0:-1])*1000000000000

#pass in "MSFT" becomes "Microsoft Corporation"
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']
#pass in company string like "Microsoft Corporation" -----> becomes "Microsoft"  
def removeCorpStrings(company):
    j=0
    while j<len(company):
        if company[j]==',':
            b=company[j+1:]
            a=company[:j]
            company = a + b
        j+=1
    sstrings = ['Holdings','Corporation','Inc','inc','Co','co','Co.','Inc.','Incororated']
    for i in sstrings:
        if company.endswith(i): 
            res = re.sub(i, '', company) 
    return res
# print(removeCorpStrings(get_symbol("MSFT"))) ----------> "Microsoft"

class Stock:
    def __init__(self, assocs = "", flt =0 , prc =0, nm = "Xxxx",tkr ="XXXX", ct= 0):
        if assocs == "":
            self.assocs = ""
        else:
            self.assocs = assocs
        if flt ==0:
            self.flt = 0
        else:
            self.flt = flt
        if prc ==0:
            self.prc=0
        else:
            self.prc = prc
        if nm == "Xxxx":
            self.nm = "Xxxx"
        else:
            self.nm = nm
        if tkr == "XXXX":
            self.tkr = "XXXX"
        else:
            self.tkr = tkr
        if ct == 0:
            self.ct =0
        else:
            self.ct = ct
    @property
    def setTicker(self,x):
        self.tkr=x
    @property
    def setFloat(self,x):
        self.flt=x
    @property
    def setPrice(self,x):
        self.prc = x
    @property
    def setAssociations(self,x):
        self.assocs=x
    @property
    def setName(self,x):
        self.name=x
    @property
    def incrementCount(self):
        self.ct+=1
    @property
    def resetCount(self):
        self.ct=0
        
    @property
    def ticker(self):
        return self.tkr
    @property
    def float(self):
        return self.flt
    @property
    def price(self):
        return self.prc
    @property
    def name(self):
        return self.nm
    @property
    def count(self):
        return self.ct
    @property
    def associations(self):
        return self.assocs
    
    def printStock(self):
        print(f'{self.tkr:6} {self.nm:15} {self.prc:5} {self.flt:13} {self.ct} {self.assocs}')



# addStock("TSLA",["Tesla","TSLA","tsla","$TSLA","Elon","elon","$tsla"],list) --------> adds a Stock object with those associations to the list
#adds stock to list. 
#t is ticker as a string, a is associations as a list else initialized to empty list
def addStock(t,a,l):
    
    parsedFloat = removeMBT(si.get_stats(t)["Value"][10])
    x = Stock(a,parsedFloat,si.get_live_price(t),removeCorpStrings(get_symbol(t)),t,0)
    tup=tuple((x.tkr,x.nm,x.prc,x.flt,x.ct,x.assocs))
    l.append(tup)
    print(f'stock {tup[0]} added to stockList')







#function to call the printStock method for each individual stock object inside a list
def printStockList(sl):
    for i in sl:
        print(f'{i} appended to stockList (list[tuple])')



#takes input into a tuple. then adds tuple to list which is the only arg
def getInpt(lst):
    print("(9 to add entries) \nAdd a stock to database using format: \nadd![ticker symbol],[association1]+[association2]+[association 3].... (you can have up to 15 associations)")
    inpt=input("For instance you could enter......... \nadd!TSLA,elon+tsla+$tsla+musk+spacex\n")
    while inpt !='9':
        #scan inputted string
        if inpt[:4]=="add!":
            i = 4
            while i < len(inpt):
                if inpt[i]==',':
                    lst.append(tuple((inpt[4:i],inpt[i+1:])))
                    print(f'{inpt[4:i]} added!')
                    break
                i+=1
        inpt=input("enter a stock or press 9 to exit\n")

def getSubInpt(lst):
    print("(9 to add entries) \nAdd a subreddit to database using format: \naddSUB![subreddit name],[# of hot posts]-[# of new posts]-[# of top (hour) posts]-[# of top (day) posts]-[# of top (week) posts]    (posts values up to 12)")
    inpt=input("For instance you could enter......... \naddSUB!wallstreetbets,5-5-5-4-3-6\n")
    while inpt !='9':
        #scan inputted string
        if inpt[:7]=="addSUB!":
            i = 7
            while i < len(inpt):
                if inpt[i]==',':
                    lst.append(tuple((inpt[7:i],inpt[i+1:])))
                    print(f'{inpt[7:i]} added!')
                    break
                i+=1
        inpt=input("enter a subreddit or press 9 to exit\n")



def addSubreddit(subnm,weightsString,l):
    i=0
    a=''
    lst=[]
    while i < len(weightsString):
        if weightsString[i] == '-':
            lst.append(a)
            a=''
        else:
            a+=weightsString[i]
        if i == len(weightsString)-1:
            lst.append(a)
        i+=1
    i=0
    while i<len(lst):
        lst[i]=int(lst[i])
        i+=1
    tup=tuple((subnm,lst[0],lst[1],lst[2],lst[3],lst[4]))
    l.append(tup)

def printSubredditList(sl):
    for i in sl:
        print(f'{i} appended to subredditList (list[tuple])')





#--------------------------------------------------------------------------------------------------------------------
