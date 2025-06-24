# 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, loops, input(), math operations, formatting, error handling
grocery_items = {
    "tomato": 2.7,
    "onion": 1.3,
    "yogurt": 2.0,
    "carrot": 1.5,
    "eggs": 2.0
}
# Step 2: Initialize dictionary to store selected items
selected_items = {}
# Step 3:Lets the user “add” items by typing their names. For each valid item, asks for the quantity.Keeps adding to the cart until the user types "checkout"
print("Welcome to the Grocery Store!")
print("Here are the available items:")
for  (item,price)in grocery_items.items():
    print(f"{item} - ${price:.2f}")
while True:
    item = input("Enter item to add (or type 'checkout' to finish): ").strip().lower()
    
    if item == "checkout":
        break
    
    if item in grocery_items:
        try:
            quantity = int(input(f"Enter quantity of {item}: "))
            if quantity > 0:
                selected_items[item]=selected_items.get(item,0)+quantity
            else:
               print("quantity should be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Item not available in store")
# Displays a final bill: each item, quantity, subtotal, and total.     
print("\n--- Final Bill ---")
total = 0
for item, quantity in selected_items.items():
    price = grocery_items[item]
    subtotal = price * quantity
    total += subtotal
    print(f"{item.title()}: {quantity} x ${price:.2f} = ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f} Vat: ${total*.15:.2f} ")
print(f"\nGrand Total: ${total*1.15:.2f}  ")