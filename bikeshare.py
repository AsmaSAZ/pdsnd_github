import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #take the city as input and validate this input also remove spaces and make it lower caee

    city= input( "Enter one of the cities:chicago, new york city or washington  ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('The input data are not valid')
        city = input("Please Select one of the city between Chicago, New York City or Washington again: ").lower()
        if city =='new york city':
            break
        else:
            city.replace(" ","")

    #Take the Month as input and validate this input
    month=input("Enter one of the months from January to June or all to display all months results ").lower().replace(" ","")
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('Not Valid')
        month = input("Please Enter a valid month value between January to June Only: ").lower().replace(" ","")

    #Take the Month as input and validate this input
    day= input("Enter one day of the week or enter the word all to display all the weekdays  ").lower().replace(" ","")
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('Not Valid')
        day = input("Please Enter a valid day value of the week Only: ").lower().replace(" ","")





    print('-'*40)
    return city, month, day





def Display_raw_data(df):
 #printing and the raw data for the user
    counter1=0
    counter2=5
 #keep a counter of the number of rows printed y.
    while True:
        Display_answer = input("Display 5 raws of the data..  yes or no?\n").lower().replace(" ","")
        if Display_answer == 'yes':
            print(df.iloc[counter1:counter2])
            counter1=counter1+5
            counter2=counter2+5
        elif Display_answer == "no": #Break the loop and continue the program
            break
          #handling if the used inter athor than yes or no
        elif Display_answer !='yes' and Display_answer != 'no':
                print("Invalid input ")
    print('-'*40)



def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #creates new column for the Month , Day and hours
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # creates new column for Month
    df['month'] = df['Start Time'].dt.month
    # creates new column for day
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # creates new column for hours
    df['hour'] = df['Start Time'].dt.hour


     # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month : ", popular_month )

    # display the most common day of week
    popular_day= df['day_of_week'].mode()[0]
    print("The most common day of the week : " , popular_day)


    # display the most common start hour
      popular_hour=df['hour'].mode()[0]
    print("the most common start hour : ", popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_Str_station= df['Start Station'].mode()[0]
    print("Most commonly used start station is: \n ",popular_Str_station)

    # display most commonly used end station
    popular_End_station= df['End Station'].mode()[0]
    print("Most commonly used end station is: \n " , popular_End_station)

    #display most frequent combination of start station and end station trip
    Frequent_combination= df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("most frequent combination of start station and end station trip: \n ",Frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('\n Total travel time: \n ', Total_travel_time, 'seconds.')

    # display average travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('\n Mean of travel time: \n ', Mean_travel_time, 'seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type= (df['User Type'].value_counts())

    # Display counts of gender
    # MAKE sure to check if the Gender is exists in the requested city data
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('\n Counts of gender is \n', counts_gender)
    else:
        print('There is no information about gender in this city')

    #Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_year = np.min(df['Birth Year'])
        print( "\n The earliest year is  ", earliest_year)
        recent_year= np.max(df['Birth Year'])
        print( "\n The most recent year is  ", recent_year )

        # Display most common year of birth
        birth_year_counts = df.groupby('Birth Year')['Birth Year'].count()
        sorted_birth_years = birth_year_counts.sort_values(ascending=False)
        most_common_birth_year = str(int(sorted_birth_years.index[0]))
        print(" \n The most common year  is  ", most_common_birth_year)

    else:
        print('This city has no information about Birth year ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        Display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
