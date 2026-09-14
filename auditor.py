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

     # Convert the valid input into an integer
    stock_quantity = int(user_input)

    # Reject negative numbers for stock quantities (kept in case input method changes later)
    if stock_quantity < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue  # skip adding this invalid entry to inventory

    # Add the valid stock quantity to the inventory
    inventory += stock_quantity
    print(f"Stock accepted. Current inventory: {inventory}")

    # Trigger overstock alert if inventory exceeds the threshold
    if inventory > 1000:
        print("Alert: Inventory exceeds the maximum threshold of 1000 units. Please review stock levels.")

print(f"Inventory: {inventory}")
print(f"Failed entries: {failed_entries}")

#Reporting 
print("\n--- Inventory Report ---")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}") 
