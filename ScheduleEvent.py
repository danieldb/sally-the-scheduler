
import datetime


class ScheduleEvent:
  def __init__(self, name, time, isAM, roughDate):
    self.name = name # some text
    self.day = roughDate # x/x/x
    self.time = time # x:xx
    self.isAM = isAM # bool
    self.year = self.getYear(roughDate)
    self.month = self.getMonth(roughDate)
    self.day = self.getDay(roughDate)
    self.hour = self.getHour(time)
    self.minute = self.getMinute(time)

    self.date = self.procTime()
    

  def getYear(self, roughDate):
    return int(roughDate.split('/')[2])
  def getMonth(self, roughDate):
    return int(roughDate.split('/')[0])
  def getDay(self, roughDate):
    return int(roughDate.split('/')[1])
  def getHour(self, time):
    return int(time.split(':')[0])
  def getMinute(self, time):
    return int(time.split(':')[1])
    
  def procTime(self):
    return datetime.datetime(self.year, self.month, self.day, (self.hour + 12*(not self.isAM)) %23, self.minute)
     