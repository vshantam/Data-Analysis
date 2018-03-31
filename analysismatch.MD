#  Match Dataset
## About Dataset:
The dataset is the <b>ipl</b> matches dataset over the years.<br>
The main objective of analysing the dataset is to find some pattern and to derive some  explanation of the matches being held over the places.<br>
<b>link:</b>(https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Match/Dataset/Match.csv)
## Analysis:

<b>1</b>
![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Match/Analysis/intern1.png)

As you can see the opponent teams have been playing quite well for a long times.i have mapped the opponent team as 0.you can see them as top right corner.<br>
May be it is a bit difficult for you to understand the ratio.let me put it this way .i will map them one above so,that you can see whose frequency is much more.<br>
![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Match/Analysis/figure_1.png)

As you can see that most of the time opponent team has won the match.<br>
<b>Note:</b> By seeing this charts what i can assume is that <b>our</b> team  is not playing upto the mark and their winning frequency is very low.According to the above chart we can derive some probabilistic relation to predeict the probability of the team.
    
      Team 1 :
              Total match count : 13
              match won by team 1: 4
              P(Team 1) :     Match won by team 1
                              --------------------
                              Total match count
                              
              P(Team 1) :     4
                              ---
                              13
                              =0.3076
                            
               P(Team 2)  = 1 - P(Team 1)
                          = 1 - 0.3076
                          = 0.6924
So The frequesncy and probabilty of the opponent team is very high and our team needs to really work hard to defeat them.

<b>2</b>

![alt_tag](https://github.com/vshantam/Data-Analysis/blob/master/Data%20Analysis/Match/Analysis/intern2.png)

This charts represents thes places where most of the maches been played acoordingly.<br>
According to the charts mostof the matches been played in the city as follows:

        1.Vishakhapatnam
        2.Mumbai
        3.Ranchi.
        and etc.
        
What i can observe from the chart is that the vishakhapatnam has the most highest frequency in the number of games played, so the chances that the next match is to be played in vizag(vishakhapatnam) is vey high among the others.

<b>Back:</b>[Click](./README.md)
