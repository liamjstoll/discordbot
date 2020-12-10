
import sqlite3
import pandas as pd


def read_from_subredditDB(subreddit,index):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    if index == 'subreddit':
        i=0
    elif index == 'hot':
        i=1
    elif index == 'new':
        i=2
    elif index == 'tophour':
        i=3
    elif index == 'topday':
        i=4
    elif index == 'topweek':
        i=5
    else:
        print("Error: DB index requested needs to be one of: 'subreddit','hot','new','tophour','topday','topweek'")
    c.execute('SELECT * FROM subreddits1 where subreddit =?',(subreddit,))
    for row in c.fetchall():
        x=row[i]
        conn.close()
        return x

        
#print(read_from_subredditDB('wallstreetbets','New'))


def print_subredditDB():
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    print(pd.read_sql_query("SELECT * FROM subreddits1", conn))
    print("----------------------\n\n")
    conn.close()

#print_subredditDB()






def insert_into_subredditDB(subredditList):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    try:
        c.executemany("INSERT INTO subreddits1 VALUES(?,?,?,?,?,?)",subredditList)
    except: # catch *all* exceptions. which obviously catches the primary key match but is bad practice, so maybe change it
        print('Already in database********')
    conn.commit()
    conn.close()


def change_subredditDB(subreddit,index,val):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    
    strin = "UPDATE subreddits1 set " + index + " = " + str(val) + " WHERE subreddit = '" + subreddit + "'"
    
    print(strin)
    c.execute(strin)
    conn.commit()
    conn.close()
    



def delete_entry_subredditDB(subreddit):
    conn = sqlite3.Connection('test.db')
    c = conn.cursor()
    # switch statement to map column names to an index in the db
    
    strin = "DELETE FROM subreddits1 WHERE subreddit = '" + subreddit + "'"
    
    print(strin)
    c.execute(strin)
    conn.commit()
    conn.close()



#dont run this function. it is run once to create a new surbeddits table
#-----------------------------------------------------------------------------------
def create_subredditDB():
    print("Subreddit database already created. To create a new one, go into the subredditDBQuery.py file, uncomment this function, and find and replace all 'subreddits1' with whatever you want the new table to be called. Then run this function again.")
    #conn = sqlite3.connect('test.db')    # should this be Connection not connect?

    #c = conn.cursor()

    #c.execute("""CREATE TABLE subreddits1 (
    #            subreddit text primary key,
    #            hot integer,
    #            new integer,
    #            tophour integer,
    #            topday integer,
    #            topweek integer
    #            )""")
    #conn.close()

#------------------------------------------------------------------------------------