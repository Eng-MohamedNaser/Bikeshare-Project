import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #get user input for city (chicago, new york city, washington).
    city=input("Please enter city name : ").lower()
    while city not in CITY_DATA:
        print("Cite name is INVALID!!!")
        city=input("Please enter correct city name : ").lower()
    print("nice you choosed '{}'".format(city.title()))
    
    
    # get user input for month (all, january, february, ... , june)
    month = input("Please enter 'all'\nor if you want to filter enter month name:").lower()
    
    while month not in months:
        print("Month name is INVALID!!!")
        month=input("Please enter 'all' or correct month name :").lower()
    print("nice you choosed",month.title())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please enter 'all'\nor if you want to filter enter day name :").lower()
    days = ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday')
    
    while day not in days:
        print("Day name is INVALID!!!")
        day=input("Please enter 'all' or correct day name :").lower()
    print("nice you choosed",day.title())
    
    print("\nYou have choosed :\nCity: {}\nMonth: {}\nDay: {}"
          .format(city,month.title(),day.title()))
    print('-'*40)
    city=CITY_DATA[city]
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data from CSV file 
    
    df = pd.read_csv(city)
    
    #creating month column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    
    #creating day column
    df['Day'] = df['Start Time'].dt.day_name()
    
    #Filter by month if not equal all
    if month !='all':
        monthIndex = months.index(month)
        df=df[df['Month'] == monthIndex]
    
    #Filter by Day if not equal all
    if day != 'all':
        day = day.title()
        df=df[df['Day']==day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    comm_month_index =df["Month"].mode()[0]
    print("Most Common Month is : {}".format(months[comm_month_index]).title())

    # display the most common day of week
    print("Most Common Day of week is : {}".format(df["Day"].mode()[0].title()))

    # display the most common start hour
    df['Hour']=df['Start Time'].dt.hour
    print("Most Common Start Hour is :",df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station is :",df['Start Station'].mode()[0])
    
    # display most commonly used end station
    print("Most Common End Station is :",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("Most Common Trip was from :-\n",
          df.groupby(['Start Station','End Station'])
          .size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Tavel Time : {} Second".format(df['Trip Duration'].sum()))
    
    # display mean travel time
    print("Mean Travel Time : {} Second".format(round(df['Trip Duration'].mean(),5)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Users Types and Counts:')
    print(df['User Type'].value_counts())
    
    
    if('Gender' in df.columns):
        # Display counts of gender
        print("")
        print('Gender Types and Counts:')
        print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth
        print("\nEarlist 'Birth Year' :",int(df['Birth Year'].min()))
        print("Mosr Reacent Year :",int(df['Birth Year'].max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def displayRowData(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start = 0
    while (view_data=='yes' and start<len(df)-5):
        print(df.iloc[start:start+5])
        start += 5
        view_data = input("Do you wish to continue? Enter yes or no? : ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displayRowData(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

