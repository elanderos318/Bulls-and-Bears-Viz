# Bulls-and-Bears-Viz

This project makes use of a python flask backend to serve S&P 500 index data from Yahoo Finance, delivered to the front-end and displayed
using D3. The idea is to display detailed information of drift and variance of index prices during "Bull" and "Bear" Markets. 

Per Investopedia:

..* "the most common definition of a bull market is a situation in which stock prices rise by 20%, usually after a drop of 20% and before a second 20% decline"
..* "A bear market is a condition in which securities prices fall 20% or more from recent highs amid widespread pessimism and negative investor sentiment"

Using these definitions as a guideline, the job of handling periods which can be considered bull or bear markets was performed using JavaScript. A line chart
displays the price changes for the S&P 500 over the data range, with blue lines indicating bull markets and red lines indicating bear markets. Then, statistical
information (mean, median min, max, Q1, Q3, IQR) can be derived for each type of market. Distributions are best displayed using histograms, and histograms were 
used to visualize information about a) the period over the entire data range, b) all periods considered "bull" markets, and c) all periods considered "bear" markets.

As an added feature, the user can adjust the definition "sensitivity"; rather than only use the commonly used '20%' rule for defining when a market changes, the user
can use whichever sensitivity he/she believes is appropriate, and the data will change accordingly.