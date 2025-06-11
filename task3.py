# Task 3: Normalize phone numbers for SMS distribution

import re

# Function to normalize phone numbers
def normalize_phone(phone_number: str) -> str:

    # Remove all non-numeric characters
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Check the length of the cleaned phone number
    match len(phone_number):
        case 9:
            # If it's 9 digits, prepend the country code for Ukraine
            return '+380' + phone_number
        case 10:
            # If it's 10 digits, prepend the country code for Ukraine
            return '+38' + phone_number
        case 12:
            # If it's already in the format with country code, return with plus sign 
            return '+' + phone_number
        case _:
            # If it doesn't match either case, return an empty value
            return None 

      

#Example raw phone numbers
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "506551234",
    "dj495jk788a"
]

# Normalize the phone numbers
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# Filter out None values from the sanitized numbers
sanitized_numbers = [item for item in sanitized_numbers if item is not None]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)