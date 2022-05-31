class Time:
    def __init__(self, month, date, hour, min):
        self.month = month
        self.date = date
        self.hour = hour
        self.min = min

    def getMonth(self):
        return self.month

    def getDate(self):
        return self.date

    def getHour(self):
        return self.hour

    def getMin(self):
        return self.min
