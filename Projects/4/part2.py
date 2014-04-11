from pandas import *
from ggplot import *
import numpy as np

def plot_weather_data(turnstile_weather):

   # Remove "R" from "Rxx"
    turnstile_weather['UNIT'] = turnstile_weather['UNIT'].map(lambda u : float(u[1:]))
    
    exits_by_station = turnstile_weather.groupby('UNIT', as_index=False).agg(
    	{'ENTRIESn_hourly' : np.median,
    	'rain' : lambda x: "Mostly No Rain" if np.mean(x) < 0.5 else "Mostly Rain"})
    print exits_by_station
    plot = (ggplot(exits_by_station, aes('UNIT', 'ENTRIESn_hourly', color='rain')) + 
            geom_point() + 
            ggtitle('Ridership by station') + 
            xlab('Station') + 
            ylab('Median number of entries per hour'))
    
    return plot

def main():

	turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
	plot = plot_weather_data(turnstile_weather)
	print plot
	plt.show(1)

if __name__ == '__main__':
	main()