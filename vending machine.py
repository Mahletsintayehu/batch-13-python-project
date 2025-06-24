#  1. Vending Machine Program
# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
# Skills practiced: loops, input(), conditionals, lists/dictionaries, sum(), print formatting
print("this ismy vending machine application")

vending_items = {
    1: ("Chips", 1.50),
    2: ("Soda", 1.00),
    3: ("Chocolate", 1.75),
    4: ("Water", 1.25),
    5: ("Gum", 0.50)
}

# Step 2: Initialize an empty list to store selected items
selected_items = []

# Step 3: Display the vending items to the user
print("Thank you for choosing us!")
print("Here are the available items:")
for number, (item, price) in vending_items.items():
    print(f"{number}. {item} - ${price:.2f}")

# Explain how to use the vending machine
print("\nTo place an order, enter the item number followed by the quantity.")
print("For example: 1 (for Chips), then 3 (for quantity).")
print("Type 'done' when you are finished.\n")

# Step 4: Loop to get user choices until they type 'done'
while True:
    choice = input("Enter item number (or type 'done' to finish): ").strip().lower()
    if choice == 'done':
        break
    # Step 5: Input validation - ensure the input is a valid item number
    if not choice.isdigit() or int(choice) not in vending_items:
        print("Invalid selection. Please enter a valid item number or 'done'.")
        continue

    item_number = int(choice)
    item_name, unit_price = vending_items[item_number]

    # Ask for quantity
    quantity_input = input(f"Enter quantity for {item_name}: ").strip()
    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("Invalid quantity. Please enter a positive number.")
        continue

    quantity = int(quantity_input)
    total_price = unit_price * quantity

    # Step 6: Add the selected item, quantity, and total price to the list
    selected_items.append((item_name, unit_price, quantity, total_price))


# Step 7: Print a formatted receipt
print("\nGroup 3 Vendor Machine\nReceipt:")
print('==================================')
grand_total = 0
for item_name, unit_price, quantity, total_price in selected_items:
    print(f"{item_name:15} ${unit_price:.2f} x{quantity:<3} - ${total_price:.2f}")
    grand_total += total_price   


# Step 8: Print the total cost
print(f"{'Total':21} - ${grand_total:.2f}")

# Calculate 15% VAT
vat = grand_total * 0.15
total_with_vat = grand_total + vat

# Display VAT and final total
print(f"{'VAT (15%)':21} - ${vat:.2f}")
print(f"{'Total Payment':21} - ${total_with_vat:.2f}")
print('==================================')
print("Thank You for Coming!")