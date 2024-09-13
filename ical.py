import csv
from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta

def parse_date(date_string):
    if date_string:
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    return None

def parse_duration(duration_string):
    if not duration_string or duration_string == "0 seconds":
        return timedelta(0)
    parts = duration_string.split(', ')
    duration = timedelta()
    for part in parts:
        value, unit = part.split()
        value = int(value)
        if 'day' in unit:
            duration += timedelta(days=value)
        elif 'hour' in unit:
            duration += timedelta(hours=value)
        elif 'minute' in unit:
            duration += timedelta(minutes=value)
    return duration

def map_priority(priority):
    if priority == "High":
        return 1
    elif priority == "Low":
        return 9
    return 5  # Default to normal priority

def csv_to_ical(csv_file, ical_file):
    cal = Calendar()
    cal.add('prodid', '-//CSV to iCal Converter//example.com//')
    cal.add('version', '2.0')

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            event = Event()
            event.add('summary', row['Label'])
            event.add('description', row.get('Summary', ''))
            
            start_date = parse_date(row.get('Start Date'))
            if start_date:
                event.add('dtstart', start_date)
            
            end_date = parse_date(row.get('End Date'))
            if end_date:
                event.add('dtend', end_date)
            elif start_date:
                duration = parse_duration(row.get('Duration', ''))
                event.add('dtend', start_date + duration)
            
            if row.get('Status'):
                event.add('status', row['Status'].upper())
            
            if row.get('Priority'):
                event.add('priority', map_priority(row['Priority']))
            
            if row.get('Tags'):
                event.add('categories', row['Tags'].split(','))
            
            if row.get('Links'):
                event.add('url', row['Links'])
            
            if row.get('Parent'):
                event.add('related-to', row['Parent'])
            
            if row.get('Project Lead'):
                event.add('attendee', f"mailto:{row['Project Lead']}@example.com")
            
            if row.get('Team'):
                event.add('attendee', f"mailto:{row['Team']}@example.com")
            
            cal.add_component(event)

    with open(ical_file, 'wb') as file:
        file.write(cal.to_ical())

# 使用示例
csv_to_ical('input.csv', 'output.ics')
