# cal-ncaa-mm

![image](https://github.com/user-attachments/assets/5079cef3-3fae-4b41-8fa0-25c3942fcd37)

Welcome to the MADNESS!!!
Calendar MADNESS!!!

That's right, it is MARCH. So, it's about time to generate those mobile event calendars for every game of the MADNESS (or sadness) ... once again!

## Brief History

It seems like every time March comes around I am looking for a reliable tool, that will simply populate my calendar with all the scheduled March Madness games. Fed-up, I rolled my own.

## Description
This tool generates a daily NCAA Basketball March Madness Tournament ICS calendar file. Each file will contain a list of individual events. There will be an event for each scheduled game on that day.

This tool also leverages the [CBBpy](https://pypi.org/project/CBBpy/) pip package to scrape the game schedules from the ncaa.com website.

## Usage 

### Generate ICS file
```
> cd src/
> ./vcal_gen.py
File '../ics/ncaa_mens_bb.ics' has been deleted.
File '../ics/ncaa_mens_bb.ics' has been created.
```

### Validate file
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

## Import calendar file
Add here.

## Example Calendar Event

This is how individual event entries in the calendar will look.

### Desktop
![image](https://github.com/user-attachments/assets/1497caec-0277-46ea-93aa-51341a9088f3)

### Mobile

