#!/usr/bin/awk -f



BEGIN {
if(!TODAY) {
   TODAY="2015-09-11-11:30:10"
}
split(TODAY, t, /[-:]/)
if(!YEAR) {
   YEAR=t[1]
}
if(!m) {
   m=t[2]
}
FS="\t"
print "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:PUBLISH"
}

function datestamp(Y,Mo,D,H,Mi,S) {
return sprintf("%04d%02d%02dT%02d%02d%02d",Y,Mo,D,H,Mi,S)
}

/PAZARTES/ { d=14 }
/SALI/ { d=15 }
/ÇARŞAMBA/ { d=16 }
/PERŞEMBE/ { d=17 }
/CUMA/ { d=18 }

{
split($3,a,/[-.]/)
print "BEGIN:VEVENT"
print "DTSTAMP:" datestamp(t[1],t[2],t[3],t[4],t[5],t[6]) "Z"
print "DTSTART:" datestamp(YEAR,m,d,a[1],a[2],0)
print "DTEND:" datestamp(YEAR,m,d,a[3],a[4],0)
print "SUMMARY:" $4
print "LOCATION:" $5
print "UID:-"m""NR"-mbg@istanbul.edu.tr"
print "DESCRIPTION:"$6
print "RRULE:FREQ=WEEKLY;COUNT=17"
print "END:VEVENT"
}

END {
print "END:VCALENDAR"
}
