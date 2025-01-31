
print("Hello, and Welcome to the Sigma Industry Hotel\n")

# Room types and availability
room_types = ["Single", "Double", "Apartment", "Suite"]
room_counts = [5, 5, 4, 2]  # Available rooms
room_prices = [400, 300, 600, 1000]  # Per adult per night
child_prices = [0, 0, 500, 800]  # Per child per night (only for apartments and suites)

# Open a file to store booking details
with open("bookings.txt", "w") as file:
    file.write("Hotel Booking Records\n")
    file.write("---------------------\n")

total_spent = 0  # Track total cost across multiple bookings

while True:
    # Show the current availability
    print("\nAvailable Rooms:")
    for i, room in enumerate(room_types):
        print(f"{room}: {room_counts[i]} rooms left")
    
    name = input("\nEnter your name: ")
    adults = int(input("Enter number of adults: "))
    children = int(input("Enter number of children: "))
    nights = int(input("Enter number of nights: "))
    total_people = adults + children

    # Choose room type
    if total_people == 1:
        room_index = 0  # Single
    elif total_people == 2:
        room_index = 1  # Double
    elif 3 <= total_people <= 4:
        print("\nAvailable Rooms:")
        print(f"1. Apartment (£{room_prices[2]} per adult/night, £{child_prices[2]} per child/night)")
        choice = input("Enter your choice (1 for Apartment): ")
        room_index = 2  # Apartment (since it's the only option)
    elif 5 <= total_people <= 6:
        print("\nAvailable Rooms:")
        print(f"1. Apartment (£{room_prices[2]} per adult/night, £{child_prices[2]} per child/night)")
        print(f"2. Suite (£{room_prices[3]} per adult/night, £{child_prices[3]} per child/night)")
        choice = input("Enter your choice (1 for Apartment, 2 for Suite): ")
        if choice == "2":
            room_index = 3  # Suite
        else:
            room_index = 2  # Apartment
    else:
        print("We can only accommodate up to 6 people per booking.\n")
        continue

    # Check room availability
    if room_counts[room_index] > 0:
        room_counts[room_index] -= 1  # Reduce available rooms

        # Calculate total cost
        cost_per_night = (adults * room_prices[room_index]) + (children * child_prices[room_index])
        total_price = cost_per_night * nights
        total_spent += total_price  # Add to total spent

        # Print receipt
        print("\n--- Booking Receipt ---")
        print(f"Customer Name: {name}")
        print(f"Room Type: {room_types[room_index]}")
        print(f"Number of Adults: {adults}")
        print(f"Number of Children: {children}")
        print(f"Number of Nights: {nights}")
        print(f"Total Price for {nights} nights: £{total_price}")
        print("----------------------\n")

        # Save booking details to file
        with open("bookings.txt", "a") as file:
            file.write(f"Customer Name: {name}\n")
            file.write(f"Room Type: {room_types[room_index]}\n")
            file.write(f"Number of Adults: {adults}\n")
            file.write(f"Number of Children: {children}\n")
            file.write(f"Number of Nights: {nights}\n")
            file.write(f"Total Price for {nights} nights: £{total_price}\n")
            file.write("----------------------\n")
    else:
        print(f"Sorry, {room_types[room_index]} is fully booked.\n")

    # Ask if the user wants to book another room
    more = input("Do you want to book another room? (yes/no): ").lower()
    if more != "yes":
        print(f"\nTotal amount spent: £{total_spent}")
        print("Thank you for booking with us!")
        break
