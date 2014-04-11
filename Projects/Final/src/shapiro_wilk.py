import numpy as np
import scipy
import scipy.stats
import pandas as pd


def shapiro_wilk(turnstile_weather):
    '''
    Returns the Shapiro-Wilk W statistic and p-value for the 
    hourly entries on days with fog, and for hourly entries on 
    days without fog. 
    '''

    with_fog = turnstile_weather[turnstile_weather['fog'] == 1]['ENTRIESn_hourly']
    without_fog = turnstile_weather[turnstile_weather['fog'] == 0]['ENTRIESn_hourly']
    
    w_fog,p_fog = scipy.stats.shapiro(with_fog)
    w_without_fog, p_without_fog = scipy.stats.shapiro(without_fog)
    
    return w_fog,p_fog,w_without_fog, p_without_fog

if __name__ == "__main__":
    input_filename = "../data/turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    w_fog,p_fog,w_without_fog,p_without_fog = shapiro_wilk(turnstile_master)

    print 'P-value for days with fog:', p_fog,w_fog
    print 'P-value for days without fog:', p_without_fog, w_without_fog