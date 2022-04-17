import datetime
import slack
import ScheduleEvent

#create class with name Schedule and a constructor
class Schedule:
  def __init__(self, bot: slack.WebClient):
    self.schedule = [] # list of events in sequential order
    self.bot = bot

  def add(self, event: ScheduleEvent):
    if len(self.schedule) == 0:
      self.schedule.append(event)
      self.bot.chat_postMessage(channel="#schedule", text="Event added!")
      return
    for i in self.schedule:
      if i.name == event.name:
        self.bot.chat_postMessage(channel="#schedule", text="Event with same name already exists")
        return
    
    if self.schedule[0].date.timestamp() < event.date.timestamp():
      self.schedule.insert(0, event)
      self.bot.chat_postMessage(channel="#schedule", text="Event added!")
      return

    for i in self.schedule:
      if i.date.timestamp() > event.date.timestamp():
        self.schedule.insert(self.schedule.index(i), event)
        self.bot.chat_postMessage(channel="#schedule", text="Event added!")
        return
  
  def remove(self, name):
    for i in self.schedule:
      if i.name == i.name:
        self.schedule.remove(i)
        self.bot.chat_postMessage(channel="#schedule", text="Event removed!")
        return
    self.bot.chat_postMessage(channel="#schedule", text="No event with that name exists, add it using /add <name> <time> <AM | PM> <MM/DD/YY>")
  
  def next(self):
    ev = 0
    val = 99999999999999999999 # a number bigger than any possible date
    for i in self.schedule:
      if i.date.timestamp() > datetime.datetime.now().timestamp() and i.date.timestamp() < val: 
        val = i.date.timestamp()
        ev = i

    if ev == 0:
      self.bot.chat_postMessage(channel="#schedule", text="No events scheduled")
      return
    self.bot.chat_postMessage(channel="#schedule", text=ev.name + " is _" + ev.date.strftime('%h %d, *%r*  (%a)')  + "_, it is *" + str(ev.date - datetime.datetime.now().replace(microsecond=0)) + "* from now")
    
  
  def fetch(self):
    shedStr = ""
    for i in self.schedule:
      shedStr += i.name + ": " + i.date.strftime('%h %d, *%r*  (%a)') + "\n"
    self.bot.chat_postMessage(channel="#schedule", text=shedStr)
