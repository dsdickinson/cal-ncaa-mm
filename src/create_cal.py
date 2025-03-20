#!/usr/bin/env python3

import requests
import datetime
from icalendar import Calendar, Event

# API endpoint (Replace with actual NCAA Basketball API URL)
API_URL = "https://api.example.com/ncaa/schedule"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_ncaa_schedule():
    """Fetch NCAA basketball schedule from the API."""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Assuming API returns JSON
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def create_ics(schedule_data, output_filename="ncaa_schedule.ics"):
    """Create an ICS file from the schedule data."""
    cal = Calendar()
    cal.add("prodid", "-//NCAA Basketball Schedule//mxm.dk//")
    cal.add("version", "2.0")

    for game in schedule_data.get("games", []):
        event = Event()
        event.add("summary", f"{game['home_team']} vs {game['away_team']}")
        event.add("description", f"Location: {game.get('location', 'TBD')}\nTV: {game.get('tv', 'TBD')}")

        # Convert time to UTC format (Adjust as needed based on API response)
        game_datetime = datetime.datetime.strptime(game["start_time"], "%Y-%m-%dT%H:%M:%S%z")
        event.add("dtstart", game_datetime)
        event.add("dtend", game_datetime + datetime.timedelta(hours=2))  # Assume 2-hour game duration
        event.add("dtstamp", datetime.datetime.now())

        cal.add_component(event)

    # Write to file
    with open(output_filename, "wb") as f:
        f.write(cal.to_ical())

    print(f"ICS file created: {output_filename}")

if __name__ == "__main__":
    schedule_data = fetch_ncaa_schedule()
    if schedule_data:
        create_ics(schedule_data)
