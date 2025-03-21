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
> ./vcal_gen.py --date 2025-03-22
File '../ics/ncaa_mens_bb_2025_03_22.ics' has been deleted.
File '../ics/ncaa_mens_bb_2025_03_22.ics' has been created.
```

### Validate file
```
> head -20 ../ics/ncaa_mens_bb_2025_03_22.ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:My Product
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
SUMMARY:(12) McNeese Cowboys / (4) Purdue Boilermakers
UID:c5645501-281a-465b-8e38-ba436cdad822
SEQUENCE:1
STATUS:CONFIRMED
TRANSP:TRANSPARENT
DTSTART:20250322T121000
DTEND:20250322T141000
DTSTAMP:20250322T141000
CATEGORIES:NCAA Men's Basketball March Madness
LOCATION:Providence, RI
DESCRIPTION:Amica Mutual Pavilion\nMen's Basketball Championship - Midwest Region - 2nd Round\n(12) McNeese Cowboys / (4) Purdue Boilermakers\n12:10 PM - 02:10 PM EDT on CBS
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

![image](https://github.com/user-attachments/assets/f26e24d5-0aef-46c0-84dd-d934ab9fe68f) <br/><br/><br/>
![image](https://github.com/user-attachments/assets/135a19a4-a7fa-4cca-b37b-f7d10578b24a) <br/><br/><br/>
![image](https://github.com/user-attachments/assets/4552f2e9-37a1-4aa3-8a75-ac9f86437ad6) <br/><br/><br/>
![image](https://github.com/user-attachments/assets/60f0bcf8-8339-4a88-a1ce-44755ff344cd) <br/><br/><br/>
![image](https://github.com/user-attachments/assets/9d3b67a0-5965-4b75-b8d5-bdd00e7d4aa7) <br/><br/>

## Calendar Events

This provides an example of how individual event entries in the calendar appear on desktop & mobile devices.

### Desktop
![image](https://github.com/user-attachments/assets/1497caec-0277-46ea-93aa-51341a9088f3)

### Mobile
![image](https://github.com/user-attachments/assets/071cdef2-3539-4e1f-97dd-4f6e84fd28d1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/user-attachments/assets/8403c82d-7e22-42ff-866f-e2c4ee828289)

## Suggested Run Cycles
First Four - run for these dates after the Sunday selection is complete. This is the Sunday before the tournament begins.<br/>
Round 1 - same as above or after the First Four games are complete.<br/>
Round 2 - run after all Round 1 games are complete.<br/>
Sweet 16 - run after all Round 2 games are complete. <br/>
Elite 8 - run after all Sweet 16 games are complete. <br/>
Final 4 - run after all Elite 8 games are complete. <br/>
Championship - run after all Final 4 games are complete. <br/>

## Disclaimer
<i>The results are only as good as the current data provided by the ncaa.com website. You will get different results based on when this tool is run. As such, this tool needs to be run at the correct times for each round.</i>

