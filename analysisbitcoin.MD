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
 
The type of approaches that i am using is called time series analysis.i will be assesing the data from the past and hopefully will be able to derive some meaningful reasults.

<b> 1. </b> 

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_1.png)

As you can see above the there is a great rise the feild of bitcoin since 2014 ( according to the dataset) and there was also the fall in between the year 2014 and the year 2015 but since after that it pcked up the pace again.The above chart represents variation of the Total BTC over past couple of years.<br>

<b> 2. </b>
![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_2.png)

This chart represents the relationship of bitcoin transactions over the years, well to be percisely the transactions increased over the period of time but there wass a drop down near about in the november in 2017. from than till now the fluctuations of the bitcoin transactions is increased and they are not much stable as before.<br>

Let me represent the average transaction chart:<br>
![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_3.png)

So, now i believe you can see the differences of the bitcoin transactions.to be more percisely here is the combined chart that represents the transaction history

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_4.png)

<b> 3. </b>

The below graph represents the number of bitcoin sent , which is not very impressive compared to the transaction graph.

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_5.png)

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_6.png)

The below chart comapres all the transactions versus bitcoin sent over the past couple of years.

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_7.png)

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_8.png)

This is zoomed version of the above chart:

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_8.1.png)

<b> 4. </b>

Now that we know that bitcoin uses <b> Block Chain </b> technology , so it is necessary to analyze the  blocks variation over the years.


![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_9.png)

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_10.png)

What we can observe from the chart that the blocks variation is stable over the years ,although there was sometimes the there was a drop (13 times ) to be percisely . but it is not that bad comparing to all those years.

<b> 5.</b>

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Bitcoin/Analysis/figure_11.png)



<b>Back</b> :[click me](./README.md)
