
import datetime


class ScheduleEvent:
  def __init__(self, name, time, isAM, roughDate):
    self.disabled = False
    self.erMessage = 'Unknown Error'
    self.name = name # some text
    if len(time.split(':')) != 2:
      self.disabled = True
      self.erMessage = "Invalid time format, try HH:MM"
      return
    if len(roughDate.split('/')) != 3:
      self.disabled = True
      self.erMessage = "Invalid date format, try MM/DD/YY"
      return
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
    if self.disabled: return
    if not roughDate.split('/')[2].isdigit():
      self.disabled = True
      self.erMessage = "Invalid year"
      return
    return int(roughDate.split('/')[2])
  def getMonth(self, roughDate):
    if self.disabled: return
    if not roughDate.split('/')[2].isdigit():
      self.disabled = True
      self.erMessage = "Invalid month"
      return
    return int(roughDate.split('/')[0])
  def getDay(self, roughDate):
    if self.disabled: return
    if not roughDate.split('/')[2].isdigit():
      self.disabled = True
      self.erMessage = "Invalid day"
      return
    return int(roughDate.split('/')[1])
  def getHour(self, time):
    if self.disabled: return
    if not time.split(':')[0].isdigit():
      self.disabled = True
      self.erMessage = "Invalid hour"
      return
    return int(time.split(':')[0])
  def getMinute(self, time):
    if self.disabled: return
    if not time.split(':')[1].isdigit():
      self.disabled = True
      self.erMessage = "Invalid minute"
      return
    return int(time.split(':')[1])
    
  def procTime(self):
    if self.disabled: return
    return datetime.datetime(self.year, self.month, self.day, (self.hour + 12*(not self.isAM)) %23, self.minute)
     