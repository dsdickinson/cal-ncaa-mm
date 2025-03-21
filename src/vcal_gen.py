#!/usr/bin/env python3

import os
import pandas as pd
from tabulate import tabulate
from datetime import timedelta

import cbbpy.mens_scraper as m
#import cbbpy.womens_scraper as w

from datetime import datetime
import pytz


pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199


def convert_to_military_time(time_12h):
	"""
	Converts a 12-hour time string (with AM/PM) to 24-hour (military) time string.

	Args:
		time_12h: A string representing time in 12-hour format (e.g., "05:48 PM", "12:00 AM").

	Returns:
		A string representing the equivalent time in 24-hour format (e.g., "17:48", "00:00").
	"""
	try:
		time_object = datetime.strptime(time_12h, "%I:%M %p")
		return time_object.strftime("%H:%M:%S")
	except ValueError:
		return "Invalid time format"

def convert_to_standard_time(military_time):
    """Converts military time to standard time.

    Args:
        military_time: A string representing time in military format (HHMM).

    Returns:
        A string representing time in standard format (HH:MM AM/PM).
    """
    hours = int(military_time[:2])
    minutes = military_time[2:]

    if hours == 0:
        standard_hours = 12
        period = "AM"
    elif hours < 12:
        standard_hours = hours
        period = "AM"
    elif hours == 12:
        standard_hours = 12
        period = "PM"
    else:
        standard_hours = hours - 12
        period = "PM"

    return f"{standard_hours}:{minutes} {period}"

def convert_pst_to_est(pst_time_str, pst_format="%Y-%m-%d %H:%M:%S"):
    """
    Converts a time string from PST to EST.

    Args:
        pst_time_str: The time string in PST.
        pst_format: The format of the PST time string (default is "%Y-%m-%d %H:%M:%S").

    Returns:
        The converted time string in EST, or None if an error occurs.
    """
    try:
        pst_timezone = pytz.timezone('US/Pacific')
        est_timezone = pytz.timezone('US/Eastern')

        # Create a datetime object from the PST time string
        pst_datetime = datetime.strptime(pst_time_str, pst_format)

        # Localize the datetime object to PST
        pst_datetime = pst_timezone.localize(pst_datetime)

        # Convert to EST
        est_datetime = pst_datetime.astimezone(est_timezone)

        # Format the EST datetime object back to a string
        est_time_str = est_datetime.strftime(pst_format)

        return est_time_str
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

def adjust_time(time_12h, hours_to_add, minutes_to_add):
	"""
	Converts a 12-hour time string (with AM/PM) to 24-hour (military) time string.

	Args:
		time_12h: A string representing time in 12-hour format (e.g., "05:48 PM", "12:00 AM").

	Returns:
		A string representing the equivalent time in 24-hour format (e.g., "17:48", "00:00").
	"""

	# 11:00 PM
	time_format = "%I:%M %p"

	try:
		existing_time = datetime.strptime(time_12h, "%I:%M %p")
		duration = timedelta(hours=hours_to_add, minutes=minutes_to_add)
		new_time = existing_time + duration
		return new_time.strftime(time_format)
	except ValueError:
		return "Invalid time format"

def convert_date_format(date_string, original_format, new_format):
    """
	Converts a date string from one format to another.

    Args:
        date_string: The date string to convert.
        original_format: The format code of the original date string.
        new_format: The format code of the desired output format.

    Returns:
        The converted date string, or None if an error occurs.
    """
    date_object = datetime.strptime(date_string, original_format)
    try:
        date_object = datetime.strptime(date_string, original_format)
        return date_object.strftime(new_format)
    except ValueError:
        return None

if __name__ == "__main__":
	head_template_file = "../templates/vcal_head.tmpl"
	event_template_file = "../templates/vcal_event.tmpl"
	tail_template_file = "../templates/vcal_tail.tmpl"

	output_file = "../ics/ncaa_mens_bb.ics"

	head_prod_id = "My Product"
	head_cal_scale = "GREGORIAN"
	head_method = "PUBLISH"

	vcal_head_values = {
		"prod_id": head_prod_id,
		"calscale": head_cal_scale,
		"method": head_method,
	}

	try:
		with open(head_template_file, "r") as head_template:
			head_template_content = head_template.read()
			head_template.close()
	except FileNotFoundError:
		print(f"Error: The file '{head_template_file}' was not found.")
		exit(1)
	except Exception as e:
		print(f"An error occurred: {e}")
		exit(1)

	try:
		with open(event_template_file, "r") as event_template:
			event_template_content = event_template.read()
			event_template.close()
	except FileNotFoundError:
		print(f"Error: The file '{event_template_file}' was not found.")
		exit(1)
	except Exception as e:
		print(f"An error occurred: {e}")
		exit(1)

	try:
		with open(tail_template_file, "r") as tail_template:
			tail_template_content = tail_template.read()
			tail_template.close()
	except FileNotFoundError:
		print(f"Error: The file '{tail_template_file}' was not found.")
		exit(1)
	except Exception as e:
		print(f"An error occurred: {e}")
		exit(1)

	# Append each game to vcal file
	try:
		if os.path.exists(output_file):
			os.remove(output_file)
			print(f"File '{output_file}' has been deleted.")
		with open(output_file, "a") as output:
			head_filled_content = head_template_content.format(**vcal_head_values)
			output.write(head_filled_content)
			#output.write(head_filled_content + "\n")

			#print(m.get_conference_schedule('ovc', 2024))
			#print(m.get_game_ids('2025/03/20'))
			game_ids = m.get_game_ids('2025/03/20')
		
			for game_id in game_ids:
				#print(game_id)
				game_info = m.get_game_info(game_id)
				#print(game_info)
				df = pd.DataFrame(game_info)
				#print(tabulate(df, headers='keys', tablefmt='psql'))
			
			
			#	print(df.game_id.values[0])
			#	print(df.game_status.values[0])
			#	print(df.home_team.values[0])
			#	print(df.home_id.values[0])
			#	print(df.home_rank.values[0])
			#	print(df.home_record.values[0])
			#	print(df.home_score.values[0])
			#	print(df.away_team.values[0])
			#	print(df.away_id.values[0])
			#	print(df.game_time.values[0])
			#	print(df.game_loc.values[0])
			#	print(df.arena.values[0])
			#	print(df.arena_capacity.values[0])
			#	print(df.attendance.values[0])
			#	print(df.tv_network.values[0])
			#	print(df.referee_1.values[0])
			#	print(df.referee_2.values[0])
			#	print(df.referee_3.values[0])
			
				this_time_zone = "PDT"
			
				# 11:00 AM
				# 01:00 PM
				regular_time_pst = df.game_time.values[0].replace(this_time_zone, "").strip()
				print(f"\nregular time pst: {regular_time_pst}")
			
				# 11:00 AM -> 11:00:00
				# 01:00 PM -> 13:00:00
				military_time_pst = convert_to_military_time(regular_time_pst)
				print(f" military time pst: {military_time_pst}")
			
				# 11:00 AM -> 01:00 PM
				# 01:00 PM -> 03:00 PM
				adjusted_time_pst = adjust_time(regular_time_pst, 2, 0)
				print(f" adjusted time pst: {adjusted_time_pst}")
			
				# March 20, 2025 11:00 AM PDT
				date_time_start = df.game_day.values[0] + " " + regular_time_pst
				print(f"date time start: {date_time_start}")
			
				# March 20, 2025 01:00 PM PDT
				date_time_end = df.game_day.values[0] + " " + adjusted_time_pst
				print(f"date time end: {date_time_end}")
			
				# YYYYMMDDTHHMMSS (%Y%m%d%Z%%H%M%S)
				# Mar 20, 2025 11:00 AM PDT -> 20250320T110000
				# DTSTART
				ical_event_start_time = convert_date_format(date_time_start, "%B %d, %Y %I:%M %p", "%Y%m%dT%H%M%S")
			
				# YYYYMMDDTHHMMSS (%Y%m%d%Z%%H%M%S)
				# Mar 20, 2025 01:00 PM PDT -> 20250320T130000
				# DTEND
				ical_event_end_time = convert_date_format(date_time_end, "%B %d, %Y %I:%M %p", "%Y%m%dT%H%M%S")
				print(ical_event_start_time)
				print(ical_event_end_time)
			
				this_event = "(" + str(df.away_rank.values[0]) + ") " + df.away_team.values[0] + " / " + "(" + str(df.home_rank.values[0]) + ") " + df.home_team.values[0]
				#this_game_time_start = df.game_time.values[0]
				this_game_time_start = regular_time_pst
				this_game_time_end = adjusted_time_pst
				print(f"\ngame_id: {game_id}")
				print(this_event)
				print(f"{this_game_time_start} - {this_game_time_end} {this_time_zone} on {df.tv_network.values[0]}")
				print(f"{df.game_loc.values[0]} - {df.arena.values[0]}")
				print(f"{df.tournament.values[0]}")
		
				event_summary = this_event
				event_uid = "00001"
				event_seq = 1
				event_status = "CONFIRMED"
				event_dtstart = ical_event_start_time
				event_dtend = ical_event_end_time
				event_dtstamp = ical_event_end_time # XXX
				event_cats = "March Madness"
				event_location = df.game_loc.values[0]
				event_description = "{} - {} {} on {}".format(this_game_time_start, this_game_time_end, this_time_zone, df.tv_network.values[0])
				event_url = "MY URL" # XXX
			
				#print(m.get_game_info(401745972))
				vcal_event_values = {
					"summary": event_summary,
					"uid": event_uid,
					"sequence": event_seq,
					"status": event_status,
					"dtstart": event_dtstart,
					"dtend": event_dtend,
					"dtstamp": event_dtstamp,
					"categories": event_cats,
					"location": event_location,
					"description": event_description,
					"url": event_url,
				}
				print(vcal_event_values)
				event_filled_content = event_template_content.format(**vcal_event_values)
				output.write(event_filled_content)
				#output.write(event_filled_content + "\n")
	
			vcal_tail_values = {}
		
			tail_filled_content = tail_template_content.format(**vcal_tail_values)
			output.write(tail_filled_content)
			#output.write(tail_filled_content + "\n")

			output.close()
	except FileNotFoundError:
		print(f"Error: The file '{output_file}' was not found.")
		exit(1)
	except Exception as e:
		print(f"An error occurred: {e}")
		exit(1)

