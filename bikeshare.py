import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    flag = True
    while flag:
        city = input('\nPlease enter the city you wish to look at (Chicago, Washington, or New York City): ').lower()
        for cit in CITY_DATA:
            if cit == city:
                flag = False
                break
        if flag:
            print('You have entered an invalid response, please try again and enter an appropriate city')

    # get user input for month (all, january, february, ... , june)
    flag = True
    while flag:
        print("\nPlease enter the month you wish to look at (January to June)")
        month = input("or enter 'all' if you want to look at every month: ").lower()
        if month != 'all':
            for mon in months:
                if mon == month:
                    flag = False
                    break
        else:
            flag = False
        if flag:
            print("\nYou have entered an invalid response. Please try again and enter 'all' or an appropriate month")
            print("Also, please enter the full name of the month (i.e. January).")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    flag = True
    while flag:
        day = input("\nPlease enter the day of the week or 'all' for every day: ").lower()
        if day != 'all':
            for d in days:
                if d == day:
                    flag = False
                    break
        else:
            flag = False
        if flag:
            print("\nYou have entered an invalid response.  Please try again and enter 'all' or an appropriate day")
            print("of the week.  Also, please enter the full name of the day (i.e. Wednesday)")


    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Also asks user if he/she wants to see raw data that is loaded.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    if month != 'all':
        for mon in months:
            if mon == month:
                monindex = months.index(month) + 1
                df = df[df['Month'] == monindex]
                break
    if day != 'all':
        for d in days:
            if d == day:
                dayindex = days.index(day)
                df = df[df['day_of_week'] == dayindex]
                break

    #Asks user if he/she wants to see the raw data loaded
    print('\nYou have loaded data from ', city.title())
    raw_response = input('Do you want to see the first five lines of data? (yes or no): ').lower()
    flag = True
    start = 0
    while flag:
        if raw_response == 'yes':
            print(df.iloc[start:start+5])
            start += 5
            raw_response = input('\nDo you want to see another five lines of raw data? (yes or no): ')
        elif raw_response == 'no':
            flag = False
        else:
            print('Please type "yes" or "no" fully')
            raw_response = input('Do you wish to see this data? (yes or no): ')

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('\nIf you inputted a "day" or "month" filter, the program will omit')
    print('outputting the most common day and/or month\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        commonmonth = df['Month'].mode()[0]
        print('The most common month is', months[commonmonth - 1].title())
    else:
        print('Since you inputted ', month.title(), ', most common month is omitted.')

    # display the most common day of week
    if day == 'all':
        commonday = df['day_of_week'].mode()[0]
        print('The most common day of the week is', days[commonday].title())
    else:
        print('Since you inputted ', day.title(), ', most common day is omitted.')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    commonhour = df['hour'].mode()[0]
    print('The most common hour is ', commonhour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    start_station_count = df['Start Station'].value_counts()[0]
    print('\nMost common start station: ', common_start)
    print('Count: ', start_station_count)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    end_station_count = df['End Station'].value_counts()[0]
    print('\nMost common end station: ', common_end)
    print('Count: ', end_station_count)

    # display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + ' + ' + df['End Station']
    common_combo = df['Start and End Station'].mode()[0]
    common_combo_count = df['Start and End Station'].value_counts()[0]
    print('\nMost frequent combination of start and end stations: ', common_combo)
    print('Count:', common_combo_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is ", total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types, '\n')

    # Display counts of gender, bypasses this if user wants to see
    # Data from Washington

    if city != 'washington':
        gender_types = df['Gender'].value_counts()
        print(gender_types)
        print()
    else:
        print("Washington has no gender data.")

    # Display earliest, most recent, and most common year of birth
    # And bypasses this if user wants to see data from Washington

    if city != 'washington':
        earliest_year = df['Birth Year'].min()
        print('Earliest birth year: ', earliest_year)
        recent_year = df['Birth Year'].max()
        print('Most recent birth year: ', recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('Most common birth year', common_year)
    else:
        print("Washington has no birth year data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
