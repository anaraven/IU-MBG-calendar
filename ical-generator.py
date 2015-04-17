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

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2005,4,4,8,0,0))
event.add('dtend', datetime(2005,4,4,10,0,0))
event.add('dtstamp', datetime(2005,4,4,0,10,0))
event.add('location', 'Odense, Denmark')
cal.add_component(event)


print cal.to_ical()
