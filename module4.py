import stockDBQuery as stockDB
import subredditDBQuery as subredditDB
import redditstockbot1 as bot



# just call the method and it asks user for input and adds it to DB
def getstocks():
    tupleList=[]
    bot.getInpt(tupleList)
    #print(tupleList)

    # list of Stock objects
    stockList = []
    for i in tupleList:
        bot.addStock(i[0],i[1],stockList)
        

    #bot.printStockList(stockList)

    stockDB.insert_into_stockDB(stockList)

    stockDB.print_stockDB()


# just call the method and it asks user for input and adds it to DB
def getsubreddits():
    tupleList=[]
    bot.getSubInpt(tupleList)
    #print(tupleList)

    # list of Stock objects
    subredditList = []
    for i in tupleList:
        bot.addSubreddit(i[0],i[1],subredditList)
    

    #bot.printSubredditList(subredditList)

    subredditDB.insert_into_subredditDB(subredditList)

    subredditDB.print_subredditDB()

def getnewassociation():
    inpt=input("Ticker of stock?\n")
    inpt2=input("association to add?:\n")
    s=stockDB.read_from_stockDB(inpt,'associations')
    s+="+"
    s+=inpt2
    k="'"+s+"'"
    
    stockDB.change_stockDB(inpt,'associations',k)
    stockDB.print_stockDB()

