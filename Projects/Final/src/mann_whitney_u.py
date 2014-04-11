import numpy as np
import scipy
import scipy.stats
import pandas as pd


def mann_whitney_plus_means(turnstile_weather):
    '''
    Returns the mean number of entries with fog, the mean number of entries 
    without fog, and the Mann-Whitney U statistic and p-value.
    '''

    with_fog = (turnstile_weather[turnstile_weather['fog'] == 1]
        ['ENTRIESn_hourly'])
    without_fog = (turnstile_weather[turnstile_weather['fog'] == 0]
        ['ENTRIESn_hourly'])
    
    with_fog_mean = np.mean(with_fog)
    without_fog_mean = np.mean(without_fog)
    
    U,p = scipy.stats.mannwhitneyu(with_fog, without_fog)
    
    return with_fog_mean, without_fog_mean, U, p

if __name__ == "__main__":
    input_filename = "../data/turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    with_fog_mean,without_fog_mean,U,p = mann_whitney_plus_means(
        turnstile_master)

    print 'Mean of days with fog:', with_fog_mean
    print 'Mean of days without fog:', without_fog_mean
    print 'U statistic:', U
    print 'Two sided P-value:',2*p
