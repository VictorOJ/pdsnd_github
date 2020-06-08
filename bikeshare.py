import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def input_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! You are welcome to the program, Let\'s explore some US bikeshare data! \n' 'Please enter the city you would like to analyze')
    print('Chicago: 1')
    print('New York: 2')
    print('Washington: 3 \n')
         # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please choose the city you would want the statistics for: ')
    city = city.lower()
    #code is used for handing unexpected input by user
    while True: 
        if city =='1' or city == 'chicago':
            print("\nYou have chosen Chicago City! Let us proceed\n")
            return 'chicago'
        if city == '2' or city == 'new york':
             print("\nYou have chosen Chicago City! Let us proceed\n")
             return 'new york city'
        elif city == '3' or city == 'washington':
            print("\nYou have chosen Chicago City! Let us proceed\n")
            return 'washington'
        else:
            print('\nPlease enter the value of 1, 2, 3 or the name of the cities\n')
            city = input('Please choose the city you would want the statistics for: ')
            city  = city.lower()
    return city
def get_time_period():
        '''
        this code asks users to create between month and day of month, day of the week or no filters 
        '''
        period = input('\nYou want to filter the data by month and the day of the month, day of the week, or you do not want to filter at all? Type "no" for no period filter.\n')
        period = period.lower()
        
        while True:
            if period == "month":
                while True:
                    day_month = input("\nDo you want to filter the data by day of the month? Type 'Yes' or 'No'\n").lower()
                    if day_month == "no":
                        print('\n The data is now being filtered by month...\n')
                        return 'month'
                    elif day_month == "yes":
                        print('\n The data is now being filtered by month and day of the month...\n')
                        return 'day_of_month'
            
            if period == "day":
                print('\n The data is now being filtered by day of the week...\n')
                return 'day_of_the_week'
            elif period == "no":
                print('\n No period filter is being applied to the data\n')
                return "none"
            period = input("\n Please choose an option between 'month', 'day', or (no) \n").lower()
        
     # TO DO: get user input for month (all, january, february, ... , june)
def get_month(m):
    if m == 'month':
        month = input('\nChoose month! January, February, March, April, May, or June? Please type the full month name.\n')
        while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june']:
             month = input('\nPlease choose between January, February, March, April, May, or June? Please type the full month name.\n')
        return month.strip().lower()
    else:
        return 'none'
    
    #This next code asks the user for a month and a day of the month
def get_month_day(df, day_m):  
    month_day = []
    if day_m == "day_of_month":
        month = month_info("month")
        month_day.append(month)
        maximum_day_month = max_day_month(df, month)
        
        while(True):
            ask_month = """ \n Which day of the month \n
            Can you type your response as an integer between 1 and 7 """
            ask_month = ask_month + str(maximum_day_month) + "\n"
            day_m = input(ask_month)
            
            try:
                day_m = int(day_m) 
                if 1 <= day_m <= mamimum_day_month:
                    month_day.append(day_m)
                    return month_day
            except ValueError:
                print("The number you entered is not a numeric value")
    else:
        return 'none'
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day(d):       # Ask user for a day
    if d == 'day_of_week':
        day = input('\nWhich day? Please type a day M, Tu, W, Th, F, Sa, Su. \n')
        while day.lower().strip() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']:
            day = input('\nPlease type a day as a choice from M, Tu, W, Th, F, Sa, Su. \n')
        return day.lower().strip()
    else:
        return 'none'

def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    """
    print('\nLoading the data... .. .. ..\n')
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day
    return df                 


def time_filters(df, time, month, week_day, md):
   print('Data is loaded. Statistics is now being computated...\n')
    
    #filter the data by month
   if time == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    #filter the data byday of the week
   if time == 'day_of_week':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]
   if time == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = md[1]
        df = df[df['day_of_month'] == day]

   return df

def max_day_month(df, month):
    # the code gets the maximum fay of the month

    months = {"january": 1, "february": 2, "march": 3, "april":4, "may": 5, "june":6}
    df = df[df["month"] == months[month]]
    max_day = max(df["day_of_month"])
    return max_day

def month_freq(df):
    '''What is the most popular month for start time?
    '''
    print('\n * What is the most popular month for bike traveling?')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[m - 1].capitalize()
    return popular_month

def day_freq(df):
    '''What is the most popular day of week for start time?
    '''
    print('\n * What is the most popular day of the week for bike rides?')
    return df['day_of_week'].value_counts().reset_index()['index'][0]

def hour_freq(df):
    '''What is the most popular hour of day for start time?
    '''
    print('\n * What is the most popular hour of the day for bike rides?')
    df['hour'] = df['Start Time'].dt.hour
    return df.hour.mode()[0]

def ride_duration(df):
    '''
    What is the total ride duration and average ride duration?
    Result:
        tuple = total ride duration, average ride durations
    '''
    print('\n * What was the total traveling done for 2017 through June, and what was the average time spent on each trip?')
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    #this code displays the sum for total trip time, mean for avg trip time
    total_ride_time = np.sum(df['Travel Time'])
    total_days = str(total_ride_time).split()[0]

    print ("\nThe total travel time on 2017 through June was " + total_days + " days \n")
    avg_ride_time = np.mean(df['Travel Time'])
    avg_days = str(avg_ride_time).split()[0]
    print("The average travel time on 2017 through June was " + avg_days + " days \n")

    return total_ride_time, avg_ride_time

def stations_freq(df):
    '''What is the most popular start station and most popular end station?
    '''
    print("\n* What is the most popular start station?\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print (start_station)
    print("\n* What is the most popular end station?\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)
    return start_station, end_station

def common_trip(df):
    '''What is the most popular trip?
    '''
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n* What was the most popular trip from start to end?')
    return result

def bike_users(df):
    '''What are the counts of each user type?
    '''
    print('\n* Types of users: subscribers, customers, others\n')
    return df['User Type'].value_counts()

def gender_data(df):
    '''What are the counts of gender?'''
    try:
        print('\n* What is the breakdown of gender among users?\n')
        return df['Gender'].value_counts()
    except:
        print('There is no gender data in the source.')
    
def birth_years(df):
    '''What is the earliest, latest, and most frequent birth year?'''
    try:
        print('\n* What is the earliest, latest, and most frequent year of birth, respectively?')
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is " + str(most_frequent) + "\n")
        return earliest, latest, most_frequent
    except:
        print('No available birth date data for this period.')

def process(f, df):

    start_time = time.time()
    statToCompute = f(df)
    print(statToCompute)
    print("Computing this stat took %s seconds." % (time.time() - start_time))

def disp_raw_data(df):
        
    df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    see_data = input("\nYou like to see rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
        
def main():
    '''The main function calculates and prints out the 
    descriptive statistics about a requested city
    '''
    # calling all the functions step by step
    city = input_city()
    df = load_data(city)
    period = get_time_period()
    month = get_month(period)
    day = get_day(period)
    month_day =get_month_day(df, period)

    df = time_filters(df, period, month, day, month_day)
    disp_raw_data(df)
    
    # all the conclusions
    stats_funcs_list = [month_freq,
     day_freq, hour_freq, 
     ride_duration, common_trip, 
     stations_freq, bike_users, birth_years, gender_data]
	
    for x in stats_funcs_list:	
        process(x, df)

    # Restarting option
    restart = input("\n * Would you like to do it again and perform another analysis? Type \'yes\' or \'no\'.\n")
    if restart.upper() == 'YES' or restart.upper() == "Y":
        main()

if __name__ == '__main__':
    main()            

