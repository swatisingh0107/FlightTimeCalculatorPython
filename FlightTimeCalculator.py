import datetime
import pytz #library to get GMT time

class FlightTimeCalculator:
    def __init__(self, airlineCode, flightNum,
                 scheduledDepTime, actualDepTime, scheduledArrTime, actualArrTime,
                 depTimeZone, arrTimeZone):
        self.airlineCode = airlineCode
        self.flightNum = flightNum

        self.checkDateTimeType(scheduledDepTime)
        self.scheduledDepTime = scheduledDepTime

        self.checkDateTimeType(actualDepTime)
        self.actualDepTime = actualDepTime

        self.checkDateTimeType(scheduledArrTime)
        self.scheduledArrTime = scheduledArrTime

        self.checkDateTimeType(actualArrTime)
        self.actualArrTime = actualArrTime

        self.depTimeZone = depTimeZone
        self.arrTimeZone = arrTimeZone

    def diffInDepartureTimes(self):
        return self.diffInTime(self.actualDepTime, self.scheduledDepTime)

    def diffInArrivalTimes(self):
        return self.diffInTime(self.actualArrTime, self.scheduledArrTime)


    def checkDateTimeType(self, inputDateTime):
        if (type(inputDateTime) != datetime.datetime):
            raise TypeError("Enter time as datetime.datetime object")

    def diffInTime(self, time1, time2):
        if(time1 > time2):
            return int((time1 - time2).seconds/60)
        else:
            return int((time2 - time1).seconds/60)

    def getFlightDuration(self):
        arrTime = self.getGMTTime(self.actualArrTime, self.arrTimeZone)
        depTime = self.getGMTTime(self.actualDepTime, self.depTimeZone)
        return int((arrTime - depTime).seconds/60)

    def getTime(self, time, timeZone):
        if timeZone != None:
            local = pytz.timezone(timeZone)
            local_dt = local.localize(time)
        else:
            local_dt = time
        utc_dt = local_dt.astimezone(pytz.utc).replace(tzinfo = None)
        return utc_dt

    def getFlightSummary(self):
        FlightIdentifier = self.airlineCode + " " + str(self.flightNum)
        DepartureDifference = self.diffInDepartureTimes()
        ArrivalDifference = self.diffInArrivalTimes()
        Duration = self.getFlightDuration()
        return FlightIdentifier, DepartureDifference, ArrivalDifference, Duration