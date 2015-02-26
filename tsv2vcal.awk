#!/usr/bin/awk -f

BEGIN {
FS="\t"
print "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:PUBLISH"
}

function datestamp(Y,Mo,D,H,Mi,S) {
return sprintf("%04d%02d%02dT%02d%02d%02d",Y,Mo,D,H,Mi,S)
}

{
split($1,a,/[-.]/)
print "BEGIN:VEVENT"
print "DTSTAMP:" datestamp(2015,02,26,11,30,10) "Z"
print "DTSTART:" datestamp(2015,m,d,a[1],a[2],0)
print "DTEND:" datestamp(2015,m,d,a[3],a[4],0)
print "SUMMARY:" $2
print "LOCATION:" $3
print "UID:-417s61147-mbg@istanbul.edu.tr"
print "DESCRIPTION:"$4
print "RRULE:FREQ=WEEKLY;COUNT=12"
print "END:VEVENT"
}

END {
print "END:VCALENDAR"
}
