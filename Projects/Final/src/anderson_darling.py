import numpy as np
import scipy
import scipy.stats
import pandas as pd


def anderson_darling(turnstile_weather):
    '''
    Returns the Shapiro-Wilk W statistic and p-value for the 
    hourly entries on days with fog, and for hourly entries on 
    days without fog. 
    '''

    turnstile_weather['ENTRIESn_hourly'] = (turnstile_weather
        ['ENTRIESn_hourly'].map(lambda e : np.log(e+1)))

    with_fog = turnstile_weather[turnstile_weather['fog'] == 1]['ENTRIESn_hourly']
    without_fog = turnstile_weather[turnstile_weather['fog'] == 0]['ENTRIESn_hourly']
    
    a2_fog,critical_fog,sig_fog = scipy.stats.anderson(with_fog, dist='norm')
    a2_without_fog,critical_without_fog,sig_without_fog = scipy.stats.anderson(without_fog, dist='norm')
    
    return a2_fog,critical_fog,sig_fog, a2_without_fog,critical_without_fog,sig_without_fog

if __name__ == "__main__":
    input_filename = "../data/turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    a2_fog,cf,sf,a2_without_fog,cwf,swf = anderson_darling(turnstile_master)

    print 'Days with fog:', a2_fog,cf,sf
    print 'Days without fog:', a2_without_fog,cwf,swf