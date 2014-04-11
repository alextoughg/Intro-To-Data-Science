import numpy as np 
import pylab 
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    turnstile_weather = pd.read_csv("../data/turnstile_data_master_with_weather.csv")
    turnstile_weather['ENTRIESn_hourly'] = (turnstile_weather
    	['ENTRIESn_hourly'].map(lambda y: np.log(1+y)))
    
    stats.probplot((turnstile_weather[turnstile_weather['fog'] == 1]
    	['ENTRIESn_hourly']), fit=0, dist="norm", plot=plt)
    plt.title('Normal probability plot of hourly ridership on foggy days')
    plt.xlabel('Theoretical normal quantiles')
    plt.ylabel('f(Hourly entries) quantiles')
    plt.savefig("../img/qqplot_fog.png")

    plt.clf()

    
    stats.probplot((turnstile_weather[turnstile_weather['fog'] == 0]
    	['ENTRIESn_hourly']), dist="norm", fit=True, plot=plt)
    plt.title('Normal probability plot of hourly ridership on non-foggy days')
    plt.xlabel('Theoretical normal quantiles')
    plt.ylabel('f(Hourly entries) quantiles')
    plt.savefig("../img/qqplot_no_fog.png")



