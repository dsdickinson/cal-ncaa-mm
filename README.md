# cal-ncaa-mm

![image](https://github.com/user-attachments/assets/5079cef3-3fae-4b41-8fa0-25c3942fcd37)

Welcome to the MADNESS!!!
Calendar MADNESS!!!

That's right, it is MARCH. Which means, it's time to generate those calendar entries for every game of the MADNESS (or sadness) ... whichever you prefer.

## Brief History

It seems like every time mid-March comes around I am looking for a reliable tool, that will simply populate my personal calendar with all the scheduled March Madness games. Fed-up, I rolled my own.

## Description
This tool generates NCAA Basketball March Madness Tournament ics calendar files that can be easily imported into any ics supported calendar. Each file contains a list of individual events. There will be an event entry for each scheduled game on a given day.

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
* Go to Google Calendar and look for "Other calendars" and hit the + sign.<br/>
* Click "Import".<br/>
* Choose the *.ics file you want to import.<br/>
* Select the calendar to add the entries to under "Add to calendar".<br/>
* Click import.<br/>

![image](https://github.com/user-attachments/assets/f26e24d5-0aef-46c0-84dd-d934ab9fe68f) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/user-attachments/assets/135a19a4-a7fa-4cca-b37b-f7d10578b24a) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/user-attachments/assets/4552f2e9-37a1-4aa3-8a75-ac9f86437ad6) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<br/><br/>
![image](https://github.com/user-attachments/assets/60f0bcf8-8339-4a88-a1ce-44755ff344cd) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/user-attachments/assets/9d3b67a0-5965-4b75-b8d5-bdd00e7d4aa7) 

## Calendar Events

This is how individual event entries in the calendar appear on desktop & mobile devices.

### Desktop
![image](https://github.com/user-attachments/assets/1497caec-0277-46ea-93aa-51341a9088f3)

### Mobile
![image](https://github.com/user-attachments/assets/071cdef2-3539-4e1f-97dd-4f6e84fd28d1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/user-attachments/assets/8403c82d-7e22-42ff-866f-e2c4ee828289)







