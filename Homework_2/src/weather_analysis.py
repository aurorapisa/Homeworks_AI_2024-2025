"""Weather Analysis Exercise"""
import pandas as pd
import matplotlib.pyplot as plt

def analyze_weather(df):
    """Task: Analyze temperature and precipitation patterns"""

    """
    # Step 1
    Calculate basic statistics:
        - Monthly temperature averages
        - Total precipitation by month
        - Seasonal patterns
        - Temperature-precipitation correlation
    """
    # Monthly temperature averages
    month_temp_avg = df.groupby('Month')['Temperature'].mean()
    # Total precipitation by month
    precipitation_by_month = df.groupby('Month')['Precipitation'].sum()

    # Correlation between Temperature and Precipitation
    correlation = df['Temperature'].corr(df['Precipitation'])

    """
    # Step 2
    Create seasonal analysis:
        - Group data by seasons
        - Calculate seasonal averages
        - Identify extreme weather months
    """
    # Prepare the statistics dictionary
    seasons = {
                 'Winter': ['Dec', 'Jan', 'Feb'],
                 'Spring': ['Mar', 'Apr', 'May'],
                 'Summer': ['Jun', 'Jul', 'Aug'],
                 'Autumn': ['Sep', 'Oct', 'Nov']
    }

    #dict comprehension, itero per ogni coppia key-value calcolo media temp e somma prec
    seasonal_averages = {
        season: {
            'Average Temperature': month_temp_avg[months].mean(),
            'Total Precipitation': precipitation_by_month[months].sum()
        }
        for season, months in seasons.items()
    }
    # Identify extreme weather months
    extreme_temp_months = {
        'Hottest': df.loc[df['Temperature'] == df['Temperature'].max(), 'Month'].values[0],
        'Coldest': df.loc[df['Temperature'] == df['Temperature'].min(), 'Month'].values[0]
    }

    extreme_prec_months = {
        'Wettest': df.loc[df['Precipitation'] == df['Precipitation'].max(), 'Month'].values[0],
        'Driest': df.loc[df['Precipitation'] == df['Precipitation'].min(), 'Month'].values[0]
    }

    """
    # Step 3
    Create visualizations:
        - Dual-axis plot for temperature and precipitation
        - Seasonal temperature averages
        - Temperature distribution
        - Temperature vs precipitation scatter plot
    """

    plt.figure(figsize=(12, 8))

    # Dual-axis plot for temperature and precipitation
    plt.subplot(2, 2, 1)
    plt.plot(month_temp_avg.index, month_temp_avg, label='Temperature', color='blue')
    plt.bar(precipitation_by_month.index, precipitation_by_month, label='Precipitation', color='orange')
    plt.xlabel('Month')
    plt.ylabel('Values')
    plt.title('Temperature and Precipitation comparison for each month')
    plt.legend()

    # Seasonal temperature averages
    seasonal_temp_averages = [seasonal_averages[season]['Average Temperature'] for season in seasons]
    plt.subplot(2, 2, 2)
    plt.bar(seasons.keys(), seasonal_temp_averages, label='Temperature')
    plt.xlabel('Season')
    plt.ylabel('Average Temperature')
    plt.title('Seasonal temperature averages')

    # Temperature distribution
    plt.subplot(2, 2, 3)
    plt.hist(df['Temperature'], color='yellow', edgecolor='black')
    plt.xlabel('Temperature')
    plt.ylabel('Frequency')
    plt.title('Temperature distribution')

    # Temperature vs precipitation scatter plot
    plt.subplot(2, 2, 4)
    plt.scatter(df['Temperature'], df['Precipitation'])
    plt.xlabel('Temperature')
    plt.ylabel('Precipitation')
    plt.title('Temperature vs Precipitation')

    plt.tight_layout()
    plt.show()

    pass