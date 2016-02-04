#!/usr/bin/python
# vim: set fileencoding=utf-8

# see <http://icalendar.readthedocs.org/en/latest/usage.html>

from icalendar import Calendar, Event
from icalendar.prop import vText
from datetime import datetime
import sys

year = 2016
month = 2
daynum = {'PAZARTESİ':8, 'SALI':9, 'ÇARŞAMBA':10, 'PERŞEMBE':11, 'CUMA':12}

title = None
prof = []
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

sem = sys.argv[1]

for fname in sys.argv[2:]:
  for line in file(fname,'r'):
    if len(line)>3:
      cmd, arg = line.strip().split(None, 1)
      # print cmd
      if cmd == 'D':
          day = arg
      elif cmd == 'S':
          if not arg.startswith(sem):
            continue
      elif cmd == 'H':
        if title is not None:
          print year, month, daynum[day], shour, smin, ehour, emin
          event = Event()
          event.add('summary', vText(title))
          description = vText(" ".join(prof))
          #event['description'] = description
          event.add('description', vText(description))
          event.add('dtstart', datetime(year, month, daynum[day],
                    int(shour), int(smin), 0))
          event.add('dtend', datetime(year, month, daynum[day],
                    int(ehour), int(emin), 0))
          event.add('dtstamp', datetime.now())
          event.add('location', vText(location))
          event.add('rrule', {"FREQ":"WEEKLY", "COUNT":"14"})
          cal.add_component(event)
        start, end = arg.split('-')
        shour,smin = start.split('.')
        ehour,emin = end.split('.')
        title = None
        prof = []
      elif cmd == 'T':
        title = arg
      elif cmd == 'L':
        location = arg
      elif cmd == 'P':
        prof.append(arg)

print cal.to_ical()
