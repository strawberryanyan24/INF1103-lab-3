# Initialize inventory and failed entries
inventory = 0
failed_entries = 0

# Continuously ask the user for stock quantities
while True:
    user_input = input("Enter stock quantity (or type 'quit' to finish): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    # Check if the input is a valid integer
    if not user_input.isdigit():
        print("Error: Please enter a valid positive whole number.")
        failed_entries += 1
        continue

    inventory += int(user_input)

print(f"Final inventory: {inventory}")
print(f"Failed entries: {failed_entries}")

# Convert the input into an integer
stock_quantity = int(user_input)

# Reject negative numbers for stock quantities
if stock_quantity < 0:
    print("Error: Stock quantity cannot be negative.")
    failed_entries += 1 

# Add the valid stock quantity to the inventory
inventory += stock_quantity

print(f"Stock accepted. Current inventory: {inventory}") 