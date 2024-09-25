import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], marker='.')

    # Create first line of best fit
    df1 = df.copy()
    params1 = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])

    # These lines of code do not appear to past the FCC test plot lines function. It appears it is testing for plt.plot instead of axline. Either will work visually though.
    '''plt.axline((0, params1.intercept), slope=params1.slope)
    plt.xlim(left=1870, right=2060)
    plt.ylim(bottom=-1)'''
    
    x1 = pd.Series([i for i in range(2014, 2051)])
    y1 = params1.slope * x1 + params1.intercept
    new1 = ({'Year': x1, 'CSIRO Adjusted Sea Level': y1})
    df1 = pd.concat([df1, pd.DataFrame(new1)], ignore_index=True)
    plt.plot(df1['Year'], params1.slope * df1['Year'] + params1.intercept)

    # Create second line of best fit
    # Filter out data range between 2000 to 2050
    mask = (df['Year'] >= 2000)
    df2 = df.copy()
    df2 = df2[mask]
    params2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])

    # Create a new data point for values between 2014 and 2051 and concatenate as a dataframe to df2
    x2 = pd.Series([i for i in range(2014, 2051)])
    y2 = params2.slope * x2 + params2.intercept
    new2 = ({'Year': x2, 'CSIRO Adjusted Sea Level': y2})
    df2 = pd.concat([df2, pd.DataFrame(new2)], ignore_index=True)
    plt.plot(df2['Year'], params2.slope * df2['Year'] + params2.intercept)

    #plt.axline((0, params2.intercept), slope=params2.slope, c='r')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()