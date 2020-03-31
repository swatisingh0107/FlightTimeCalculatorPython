## Project Objective
This simple project takes an input file in csv and return a csv file with Flight Summary Information.
The flight summary includes the following information
```
1. Flight identifier
2. Departure difference (Difference in actual and scheduled departure time)
3. Arrival difference (Difference in actual and scheduled arrival time)
4. Flight duration (Difference between actual departure and actual arrival)
```
## Before you start
**Pre-requisites**
1. You have [Python 3.7.x](https://www.python.org/downloads/) installed
2. Download FlightTimeCalculator.zip project

## Execution Instruction
1. Run ```cmd```
2. Check python version
    ```
    > python --version
    Python 3.7.2
    ```
3. Unzip the project folder in your working directory
4. Navigate to the working directory in command line
   ```
    > echo 'Install pandas'
    > setup.sh
    > echo 'Run script ReadFlightsCSV.py'
    > python ReadFlightsCSV.py
    > echo 'View output'
    > output.csv 
    ```
5. To run unittests run the following commands from the working directory:
    ```
    > python -m unittest Tests.test_FlightTimeCalculator
    > python -m unittest Tests.test_TimeZoneCalculator
    ```
    
    
## About ReadFlights.py
This scripts reads from an input file and performs the following actions on the records
1. Verify if file exists
2. Converts arrival and departure times into date-time object
3. If any of the arrival or departure time is missing, it assumes that the actual and scheduled times are the same.
4. Executes ```FlightTimeCalculator.getFlightSummary``` on each row and appends to a dataframe
5. Outputs the result as csv file




