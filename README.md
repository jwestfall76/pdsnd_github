### Date created
Date Created: 10-10-2020

### Project Title
Bikeshare program

### Description
The program loads data from either New York City, Washington, D.C., and Chicago.  
depending on what city the user chooses.  Next, it asks the user to input
a month from January to June or "all" to include all months from January to
June. Then the program requests what day of the week the user wants to look at or
"all" for every day of the week.  

Based on the city, month, and day of the week the user picks, the program
creates a dataframe on this information.  It will then ask the user if he/she
wants to see the raw data from this dataframe in iterations of five rows until
the user wishes to continue with calculating the bikeshare data.

The program, then, will calculate the following statistics:

-   The most common month of travel unless user picked a specific
    month
-   The most common day of the week of travel unless user selected
    a specific day
-   Most common starting hour
-   Most common starting station
-   Most common ending station
-   Most common starting and ending station combination
-   Total travelling time overall
-   Average travelling time from starting station to ending station
-   Counts user types
-   Counts based on gender unless user selects Washington, D.C.
-   Earliest birth year (omitted if user picks Washington, D.C.)
-   Most recent birth year (omitted if user picks Washington, D.C.)
-   Most common birth year (omitted if user picks Washington, D.C.)

Finally, after displaying all of the calculated data, the program will ask the
user if he or she wants to run the program again.  If the user enters "no",
the program terminates.

### Files used
bikeshare.py, chicago.csv, new_york_city.csv, washington.csv, README.md,

### Credits
N/A
