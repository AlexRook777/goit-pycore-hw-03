#Task 1: Calculate the number of days from today to a given date
from datetime import datetime
 
# Function to calculate the number of days from today to a given date
def get_days_from_today(date, date_format="%Y-%m-%d"):
    try:
        # Convert the date string to a datetime object
        input_date = datetime.strptime(date, date_format)
        today = datetime.today()
        # Calculate the difference in days
        delta = (today - input_date).days
    except:
        # If the date format is incorrect or any other error occurs, set delta to None
        delta = None
    return delta

if __name__ == "__main__": # to allow import without executing the code
    input_date = "2025-06-30"
    # Calculate the number of days from today to the input date
    days_difference = get_days_from_today(input_date)   
    print(f"Days from today to {input_date}: {days_difference}") if days_difference is not None else print("Invalid date format")