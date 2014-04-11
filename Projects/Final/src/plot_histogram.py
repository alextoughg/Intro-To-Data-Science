import pandas as pd
from ggplot import *
import numpy as np


def boxcox1p(y):
    return np.log(y+1)

def entries_histogram(turnstile_weather, fog=False):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, lets 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Why don't you plot two histograms on the same axes, showing hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to the following graph:
    http://i.imgur.com/9TrkKal.png
    
    You can read a bit about using matplotlib and pandas to plot
    histograms:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can look at the information contained within the turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    '''
    plot = (ggplot(turnstile_weather, aes(x='ENTRIESn_hourly')) + 
            geom_histogram(data=turnstile_weather[turnstile_weather['fog']==0], position="identity") + 
            ggtitle('Hourly ridership') + 
            xlab('Hourly entries') + 
            ylab('Frequency'))
    '''

    #turnstile_weather['ENTRIESn_hourly'] = np.log(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['ENTRIESn_hourly'] > 0])
    turnstile_weather['ENTRIESn_hourly'] = turnstile_weather['ENTRIESn_hourly'].map(lambda y: boxcox1p(y))

    if fog:
        plot = (ggplot(turnstile_weather[turnstile_weather['fog'] == 0], 
            aes(x='ENTRIESn_hourly')) + 
            geom_histogram(color='red') +
            ggtitle('Hourly ridership on non-foggy days') + 
            xlab('log(Hourly entries+1)') + 
            ylab('Frequency'))
    else:
        plot = (ggplot(turnstile_weather[turnstile_weather['fog'] == 1], 
            aes(x='ENTRIESn_hourly')) + 
            geom_histogram(color='blue') +
            ggtitle('Hourly ridership on foggy days') + 
            xlab('log(Hourly entries+1)') + 
            ylab('Frequency'))
    
    
# What about fog option?
# Can we measure how correlated fog and rain? 
# Could we find out the level of fog from the meantempi and dewpointi? This would 
# be hard to predict? 
# BE SIMPLE AND ENJOY THE FLOP. TAKE FOG!
# STOP TRYING TO PREDICT THE FUTURE AND COVER YOUR ASS!

    return plot


   


if __name__ == "__main__":
    fog_ridership_histogram = "../img/fog_ridership_histogram.png"
    no_fog_ridership_histogram = "../img/no_fog_ridership_histogram.png"
    turnstile_weather = pd.read_csv("../data/turnstile_data_master_with_weather.csv")
    gg =  entries_histogram(turnstile_weather) 
    ggsave(no_fog_ridership_histogram, gg)
    gg =  entries_histogram(turnstile_weather, True) 
    ggsave(fog_ridership_histogram, gg)



