# cal-ncaa-mm

![image](https://github.com/user-attachments/assets/f8075341-1109-4311-b04d-bf346f027351)



Creates an ics calendar for the NCAA Basketball March Madness Tournament.

This app uses the CBBpy pip package to scrape the game schedules from the ncaa.com website.

### Run 
```
> cd src/
> ./vcal_gen.py
File '../ics/ncaa_mens_bb.ics' has been deleted.
File '../ics/ncaa_mens_bb.ics' has been created.
```

### Validate
```
> head -20 ../ics/ncaa_mens_bb.ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:My Product
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
SUMMARY:(9) Creighton Bluejays / (1) Auburn Tigers
UID:0f89f481-94a0-431d-8801-c629f0c63039
SEQUENCE:1
STATUS:CONFIRMED
TRANSP:TRANSPARENT
DTSTART:20250322T000000
DTEND:20250322T020000
DTSTAMP:20250322T020000
CATEGORIES:NCAA Men's Basketball March Madness
LOCATION:Lexington, KY
DESCRIPTION:Rupp Arena\nMen's Basketball Championship - South Region - 2nd Round\n(9) Creighton Bluejays / (1) Auburn Tigers\n12:00 AM - 02:00 AM EDT on
URL:https://github.com/dsdickinson/cal-ncaa-mm
END:VEVENT
BEGIN:VEVENT
...
```

### Example Calendar Event

This is how individual event entries in the calendar will look.

![image](https://github.com/user-attachments/assets/1497caec-0277-46ea-93aa-51341a9088f3)
