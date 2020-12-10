

#FILE -----> test.db
#TABLE ----> stocks4


import sqlite3
import pandas as pd







def read_from_stockDB(ticker,index):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    if index == 'ticker':
        i=0
    elif index == 'name':
        i=1
    elif index == 'price':
        i=2
    elif index == 'float':
        i=3
    elif index == 'count':
        i=4
    elif index == 'associations':
        i=5
    else:
        print("Error: DB index requested needs to be one of: 'ticker','name','price','float','count','associations'")
    c.execute('SELECT * FROM stocks4 where ticker =?',(ticker,))
    for row in c.fetchall():
        x=row[i]
        conn.close()
        return x

        

def print_stockDB():
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    print(pd.read_sql_query("SELECT * FROM stocks4", conn))
    print("----------------------\n\n")
    conn.close()






def insert_into_stockDB(stockList):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    try:
        c.executemany("INSERT INTO stocks4 VALUES(?,?,?,?,?,?)",stockList)
    except: # catch *all* exceptions. which obviously catches the primary key match
        print('Already in database********')
    conn.commit()
    conn.close()



def change_stockDB(ticker,index,val):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    
    strin = "UPDATE stocks4 set " + index + " = " + str(val) + " WHERE ticker = '" + ticker + "'"
    
    print(strin)
    c.execute(strin)
    conn.commit()
    conn.close()


def delete_entry_stockDB(ticker):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    
    strin = "DELETE FROM stocks4 WHERE ticker = '" + ticker + "'"
    
    print(strin)
    c.execute(strin)
    conn.commit()
    conn.close()


#cant run this function. it is run once to create a new stocks table
#-----------------------------------------------------------------------------------

def create_stocksDB():
    print("Stock database already created. To create a new one, go into the stockDBQuery.py file, uncomment this function, and find and replace all 'stocks4' with whatever you want the new table to be called. Then run this function again.")


#    conn = sqlite3.connect('test.db')

#    c = conn.cursor()

#    c.execute("""CREATE TABLE stocks4 (
#                ticker text primary key,
#                name text,
#                price real,
#                float real,
#                count integer,
#                associations text
#                )""")
#    conn.close()

#------------------------------------------------------------------------------------