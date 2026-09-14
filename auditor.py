# Initialize inventory and failed entries 
inventory = 0 
failed_entries = 0

# Continuously ask the user for stock quantities 
while True: 
    user_input = input("Enter stock quantity (or type 'quit' to finish): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break