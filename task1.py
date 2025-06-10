from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta = (today - input_date).days
    except:
        delta = None
    return delta

input_date = "2025-06-30"
days_difference = get_days_from_today(input_date)   
print(f"Days from today to {input_date}: {days_difference}") if days_difference is not None else print("Invalid date format")