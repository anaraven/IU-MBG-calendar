#!/usr/bin/python

# see <http://icalendar.readthedocs.org/en/latest/usage.html>

from icalendar import Calendar, Event
from icalendar.prop import vText
from datetime import datetime

cal = Calendar()
cal.add('version', '2.0')
cal.add('prodid', '-//calendar generator//mbg.istanbul.edu.tr//')

# TODO: 
# - parse input
# - choose good summary
# - add description
# - add alarm
# ? add sequence
# - add UID (md5?)

for line in file('seminars.txt','r'):
  date, author, subject = line.strip().split("\t")
  day, month, year = date.split(".")
  event = Event()
  event.add('summary', 'Seminar ' + author)
  #description = vText(subject)
  #event['description'] = description
  event.add('description', subject)
  event.add('dtstart', datetime(int(year), int(month), int(day), 13, 30, 0))
  event.add('dtend', datetime(int(year), int(month), int(day), 14, 30, 0))
  event.add('dtstamp', datetime.now())
  event.add('location', 'MBG-II')
  cal.add_component(event)


print cal.to_ical()
