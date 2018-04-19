<h1> Bitcoin </h1>

### Introduction 

Bitcoin is a cryptocurrency and worldwide payment system. It is the first decentralized digital currency, as the system works without a central bank or single administrator.<br>

 <b> coins :</b>Unspent outputs of transactions (in multiples of a satoshi <br>
 <b> Ledger start</b>: 3 January 2009 (9 years ago)<br>
 <b>Founder:</b> Satoshi Nakamoto
 
 ### About Dataset
 
 The dataset which i am using in this analysis is taken from quandl.<br>
 [click me](https://www.quandl.com/data/BITCOINWATCH-Bitcoin-Watch) to follow the dataset on quandl and it is not premium content.
 if you are using python then you can directly sync to qundl using quandl API.<br>I will suggest you to get your own API key using this [link](https://www.quandl.com/account/api)
 
 Here is the python code to get the above dataset :
  
      tok = ""# make sure you use your own token
      quandl.get("BITCOINWATCH/MINING", authtoken=tok)
 Use the above line in your script directly and you are good to go.
 
 ### Type of approach
 
The type of approaches that i am using is colled time series analysis.i will be assesing the data from the past and hopefully will be able to derive some meaningful reasults.

<b> 1. </b> 

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_1.png)

<b>Back</b> :[click me](./README.md)
