from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):

    turnstile_weather.DATEn = pandas.to_datetime(turnstile_weather.DATEn)
    by_hour = turnstile_weather.groupby('Hour', as_index=False)
    entries_exits_by_hour = by_hour.agg({'ENTRIESn_hourly' : sum, 'EXITSn_hourly' : sum })
    plot = (ggplot(entries_exits_by_hour, aes('Hour', 'ENTRIESn_hourly')) + geom_point(aes(shape='EXITSn_hourly')))

    return plot

def main():

	turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
	plot = plot_weather_data(turnstile_weather)
	plot.draw()

if __name__ == '__main__':
	main()