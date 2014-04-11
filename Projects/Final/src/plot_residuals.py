from predictions import *
from ggplot import *
import pylab 
import scipy.stats as stats
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    

    turnstile_weather['Residual'] = (turnstile_weather['ENTRIESn_hourly'] - predictions)

    '''
    plot = (ggplot(turnstile_weather, 
            aes(x='Residual')) + 
            geom_histogram(color='green', binwidth=1) +
            ggtitle('Hourly entries residuals') + 
            xlab('Difference between original hourly entries and predicted values') + 
            ylab('Frequency'))

    return plot
    '''

    stats.probplot((turnstile_weather
        ['Residual']), dist="norm", plot=plt)
    plt.title('Normal probability plot of hourly entries residuals')
    plt.xlabel('Theoretical normal quantiles')
    plt.ylabel('Residual quantiles')
    return plt


if __name__ == "__main__":
    input_filename = "../data/turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    #residuals_histogram = "../img/residuals.png"
    #gg = plot_residuals(turnstile_master, predicted_values)
    #ggsave(residuals_histogram, gg)

    p = plot_residuals(turnstile_master, predicted_values)

    p.savefig("../img/qqplot_residuals.png")