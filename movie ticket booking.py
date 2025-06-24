# 4. Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say “no” and displays total bookings and cost.
# Skills practiced: loops, input, conditionals, calculations, nested dictionaries

# Define available movies with showtimes and prices
movies = {
    1: {"title": "Inception", "showtime": "5:00 PM", "price": 10.00},
    2: {"title": "The Matrix", "showtime": "7:30 PM", "price": 12.50},
    3: {"title": "Interstellar", "showtime": "9:00 PM", "price": 11.00},
    4: {"title": "The Lion King", "showtime": "4:00 PM", "price": 8.00}
}

total_tickets = 0
total_cost = 0.0

print("🎟️ Welcome to the Movie Theater Booking System!\n")

# Show available movies
def show_movies():
    print("Available Movies:")
    for num, info in movies.items():
        print(f"{num}. {info['title']} - Showtime: {info['showtime']} - ${info['price']:.2f} per ticket")

# Booking loop
while True:
    show_movies()

    try:
        choice = int(input("\nEnter the number of the movie you want to book: "))
        if choice not in movies:
            print("❌ Invalid choice. Try again.")
            continue
        selected_movie = movies[choice]

        tickets = int(input(f"How many tickets for '{selected_movie['title']}'? "))
        if tickets <= 0:
            print("❌ Please enter a positive number.")
            continue

        cost = selected_movie["price"] * tickets
        total_tickets += tickets
        total_cost += cost

        print(f"✅ Booked {tickets} ticket(s) for '{selected_movie['title']}' at ${cost:.2f}")

        again = input("Do you want to book another movie? (yes/no): ").strip().lower()
        if again != "yes":
            break

    except ValueError:
        print("⚠️ Please enter valid numeric input.")

# Final Summary
print("\n🎬 Booking Summary:")
print(f"Total tickets booked: {total_tickets}")
print(f"Total cost: ${total_cost:.2f}")
print("Thank you for booking with us!")