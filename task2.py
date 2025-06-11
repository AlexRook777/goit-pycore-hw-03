# Task 2: Create a function that generates a lottery ticket with unique random numbers.
from random import random

# Function to generate a lottery ticket with unique random numbers
def get_numbers_ticket(min=1, max=49, quantity = 6):     
    # Using a set to ensure uniqueness
    ticket = set() 

    # Validate input parameters
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return ticket # Invalid parameters, return empty set
    
    # Generate given quantity of unique random numbers and add to the set
    while len(ticket) < quantity:
        ticket.add(int(random() * (max - min + 1)) + min) 
    
    #return sorted to have a consistent order
    return sorted(ticket) 

# Example usage
if __name__ == "__main__": # to allow import without executing the code
    # Generate a lottery ticket with default parameters
    ticket = get_numbers_ticket()
    print(f"Generated lottery ticket 6 from 49: {ticket}")
    
    # Example with custom parameters
    custom_ticket = get_numbers_ticket(min=1, max=36, quantity=5)
    print(f"Generated lottery ticket 5 from 36: {custom_ticket}")
