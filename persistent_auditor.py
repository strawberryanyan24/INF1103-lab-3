# ---- Global counter for failed/rejected entries ----
failed_entries = 0
 
 
def get_valid_input():
    """Prompts and validates input. Returns a valid int, or 'quit'."""
    global failed_entries
 
    while True:
        user_input = input("Enter stock quantity (or type 'quit' to finish): ")
 
        # Check if the user wants to stop
        if user_input.lower() == "quit":
            return "quit"
 
        # Validate the input is a whole number
        if not user_input.isdigit():
            print("Error: Please enter a valid positive whole number.")
            failed_entries += 1
            continue  # ask again
 
        return int(user_input)
 
 
def process_delivery(current_total, new_value):
    """Adds new_value to current_total. Returns the updated total."""
    return current_total + new_value
 
 
def calculate_tax(amount):
    """Calculates 10% tax on a single delivery amount."""
    return amount * 0.10
 
 
def generate_report(total_units, deliveries_processed, failed_attempts):
    """Prints the final summary report."""
    print("\n--- Delivery Report ---")
    print(f"Total Units in Inventory: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
 
 
# ---- Main program ----
inventory = 0
deliveries_processed = 0
 
while True:
    result = get_valid_input()
 
    if result == "quit":
        break
 
    inventory = process_delivery(inventory, result)
    tax = calculate_tax(result)
    deliveries_processed += 1
 
    print(f"Stock accepted. Current inventory: {inventory} | Tax: {tax:.2f}")
 
    if inventory > 1000:
        print("Alert: Inventory exceeds the maximum threshold of 1000 units. Please review stock levels.")
 
generate_report(inventory, deliveries_processed, failed_entries)