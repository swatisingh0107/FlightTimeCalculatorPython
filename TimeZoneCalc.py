import pandas as pd
import os

class TimeZoneCalc:
    def __init__(self, filepath, airportCodeColName, timeZoneColName):
        try:
            os.path.exists(filepath)
            self.airport = pd.read_csv(filepath)
        except FileNotFoundError:
            print(f'File {filepath} does not exist.')
            exit()

        self.timezone = dict(zip(self.airport[airportCodeColName], self.airport[timeZoneColName]))



    def getTimeZone(self,AirportCode):
        return self.timezone.get(AirportCode)
