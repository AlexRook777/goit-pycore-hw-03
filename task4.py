#Task 4: Create a function to get upcoming birthdays within the next week
from datetime import datetime
import re

def replace_delimiters_with_dashes(data_string: str) -> str:
    """
    Replace all delimiters in the input string with dashes.
    Delimiters include spaces, tabs, newlines, and commas.
    Removes any leading or trailing dashes from the final string for a cleaner result.
    """
    return re.sub(r'[ \-/\.\\,\t\n\(\)\[\]\{\}]+', '-', data_string).strip('-')

def get_days_from_next_birthday(date):
    try:
        # Convert the date string to a standard format
        # Replace delimiters with dashes to standardize the date format
        birthday = datetime.strptime(replace_delimiters_with_dashes(date), "%Y-%m-%d")
        today = datetime.today()
        # Set the birthday to this year
        next_birthday = birthday.replace(year=today.year)

        # If the birthday has already occurred this year, set it to next year
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        
        # Check if the next birthday falls on a weekend (Saturday or Sunday)
        if next_birthday.weekday() in [5, 6]:  # If birthday is on Saturday or Sunday
            # If it does, shift it to the next Monday
            next_birthday = next_birthday.replace(day=next_birthday.day + (7 - next_birthday.weekday()))

        # Calculate the difference in days 
        # between today and the next birthday
        delta = (next_birthday - today).days
    except:
        delta = None
    return delta

# Task 4: Create a function to get upcoming birthdays within the next week
# and generate a notification message for each.
def get_upcoming_birthdays_notification(users):
    upcoming_birthdays = []
    # Iterate through the list of users
    # and calculate the days until their next birthday
    for user in users:
        name = user.get("name")
        birthday_str = user.get("birthday")
        # Skip users with missing name or birthday
        if not name or not birthday_str:
            continue
        # Calculate days until next birthday
        days_till_next_birthday = get_days_from_next_birthday(birthday_str)
        #print(f"Days from today to {birthday_str} for {name}: {days_till_next_birthday}") if days_till_next_birthday is not None else print(f"Invalid date format for {name}")
        if days_till_next_birthday is not None and 0 <= days_till_next_birthday <= 7:
            upcoming_birthdays.append(f"Привітання для {name} з нагоди дня народження {birthday_str}")  
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.06.17"},
    {"name": "Alice Johnson", "birthday": "1992.12.05"},
    {"name": "Bob Brown", "birthday": "1988.06.14"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "", "birthday": "1990.03.27"},
    {"name": "Jack Smith", "birthday": "27.01.1990"}
]

# Get the list of upcoming birthdays notifications
upcoming_birthdays_notification = get_upcoming_birthdays_notification(users)
print("Список привітань на цьому тижні:", upcoming_birthdays_notification)

