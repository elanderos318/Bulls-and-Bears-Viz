import os

import pandas as pd
import numpy as np

import datetime as dt

import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bulls_bears.sqlite"

engine = create_engine('sqlite:///db/bulls_bears.sqlite', echo=False)

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

# Declare a Base using automap_base()
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)  
# Assign the table classes to variables
SP_500 = Base.classes.sp_data_v2


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

'''

##########Treasury Yield Dataset
#set up as pandas dataframe and rename variables
Treasury_Yield_DF = pd.DataFrame(engine.execute("SELECT * FROM Treasury_Yield").fetchall())
Treasury_Yield_DF = Treasury_Yield_DF.rename(columns={0: "date", 1: "R_3M", 2: "R_6M", 
                                                      3: "R_1Y", 4: "R_2Y", 5: "R_3Y",
                                                      6: "R_5Y", 7: "R_7Y", 8: "R_10Y"})

#convert pandas dataframe to json
Treasury_Yield_Json = Treasury_Yield_DF.to_json(orient='records')


##########November to January Tweets Dataset
#set up as pandas dataframe and rename variables
Nov_Jan_Tweets_DF = pd.DataFrame(engine.execute("SELECT * FROM nov_jan_tweets").fetchall())
Nov_Jan_Tweets_DF = Nov_Jan_Tweets_DF.rename(columns={0: "tweet", 1: "Date", 2: "Month", 3: "Day", 4: "Year", 5: "User"})
Nov_Jan_Tweets_DF = Nov_Jan_Tweets_DF["tweet"]

#convert pandas dataframe to json
Nov_Jan_Tweets_Json = Nov_Jan_Tweets_DF.to_json(orient='records')


##########January to March Tweets Dataset
#set up as pandas dataframe and rename variables
Jan_Mar_Tweets_DF = pd.DataFrame(engine.execute("SELECT * FROM jan_mar_tweets").fetchall())
Jan_Mar_Tweets_DF = Jan_Mar_Tweets_DF.rename(columns={0: "tweet", 1: "Date", 2: "Month", 3: "Day", 4: "Year", 5: "User"})
Jan_Mar_Tweets_DF = Jan_Mar_Tweets_DF["tweet"]

#convert pandas dataframe to json
Jan_Mar_Tweets_Json = Jan_Mar_Tweets_DF.to_json(orient='records')


# ##########S&P 500 Dataset
# #set up as pandas dataframe and rename variables
SAP500_DF = pd.DataFrame(engine.execute("SELECT * FROM SAP500").fetchall())
SAP500_DF = SAP500_DF.rename(columns={0: "Date", 1: "Open", 2: "High", 3: "Low", 4: "Close", 5: "Adj_Close", 6: "Volume"})

# #convert pandas dataframe to json
SAP500_json = SAP500_DF.to_json(orient='records')

'''


#set up routes
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/1")
def one():
    """Return the homepage."""
    return render_template("index_orig.html")

@app.route("/sap500")
def sap500():
    """Return the homepage."""
    return render_template("sap500.html")

@app.route("/treasuryyields")
def yields():
    """Return """
    return(jsonify(Treasury_Yield_Json))

@app.route("/Nov_Jan_Tweets")
def Nov_Jan_Tweets():
    """Return """
    return(jsonify(Nov_Jan_Tweets_Json))

@app.route("/Jan_Mar_Tweets")
def Jan_Mar_Tweets():
    """Return """
    return(jsonify(Jan_Mar_Tweets_Json))

@app.route("/sp_line_init")
def sp_line_init():
    
    session = Session(engine)

    line_query = session.query(SP_500.date, SP_500.close)
    
    line_list = []
    keys = ("date", "close")

    # Iteration for converting sqlalchemy date response into date string and appening to list
    for query in line_query:
        list_query = list(query)
        list_query[0] = dt.datetime.strftime(list_query[0], "%Y-%m-%d")
        line_dict = dict(zip(keys, list_query))
        line_list.append(line_dict)

    session.close()

    line_json = json.dumps(line_list)

    return line_json

@app.route("/stock_tracker")
def stock_tracker():
    return render_template('stock_tracker.html')



'''
@app.route("/sap500_data")
def sap500_route():
    """Return """
    return(jsonify(SAP500_json))
'''


if __name__ == "__main__":
    app.debug = True
    app.run()