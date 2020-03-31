import pandas as pd
import TimeZoneCalc
import FlightTimeCalculator as ft
import datetime

flights = pd.read_csv("flights.csv")
airport = TimeZoneCalc.TimeZoneCalc("airports.csv", "Airport code", "Time zone")

data = []
for index, row in flights.iterrows():
    if pd.isnull(row[4]):
        row[4] = row[5]
    elif pd.isnull(row[5]):
        row[5] = row[4]

    if pd.isnull(row[6]):
        row[6] = row[7]
    elif pd.isnull(row[7]):
        row[7] = row[6]
    # Convert date-time string fields into datetime objects
    schedDepTime = datetime.datetime.strptime(row[4], "%Y-%m-%dT%H:%M:%S")
    actDeptTime = datetime.datetime.strptime(row[5], "%Y-%m-%dT%H:%M:%S")
    schedArrTime = datetime.datetime.strptime(row[6], "%Y-%m-%dT%H:%M:%S")
    actArrTime = datetime.datetime.strptime(row[7], "%Y-%m-%dT%H:%M:%S")

    ftobject = ft.FlightTimeCalculator(row[0], row[1], schedDepTime, actDeptTime,
                                       schedArrTime, actArrTime, airport.getTimeZone(row[2]),
                                       airport.getTimeZone(row[3]))
    data.append(ftobject.getFlightSummary())

data = pd.DataFrame(data, columns=('Flight identifier', 'Departure difference', 'Arrival difference', 'Duration'))
output = data.to_csv(r'output.csv', index=None, header=True)
