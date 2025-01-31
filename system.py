print("Hello, and Welcome to the Sigma Industry Hotel")
print("")

rooms = 10
single = 5
double = 5
apartment = 4
small = 2
medium = 2

print ("Total Number of Rooms available: ", rooms)

print (f"-Deluxe Single Room: {single} rooms left")
print (f"- Deluxe Double Room (For 2): {double} rooms left")
print (f" - Per Adult: £400")
print (f" - Per Adult: £300")
print("")
print (f"- Signature Apartment(Up to 6 people): {apartment} rooms left.")
print (f" - Per Adult: £600")
print (f" - Per Adult: £500")
print("")
print (f"- Presidential Suite (For the recognised ONLY)")
print (f"   - Small Suite(For 1): {small} rooms left")
print (f"   - Medium Suite(For 2): {medium} rooms left")
print (f"       - Per Adult: £1000")
print (f"       - Per Child: £800")

adults = int(input("Enter number of adults: "))
child = int(input("Enter number of children: "))

if adults + child == 1:
    chosen = single

if adults + child == 2:
    chosen = double

if adults + child == 3:
    print("Which room do you want to book?")
    print("- Deluxe Double")
    print("- Signature Apartment")
    print("")
    chosen = input("Enter choice: ")


# Welcome message
print("Hello, and Welcome to the Sigma Industry Hotel\n")

# Room availability
rooms = {
    "single": 5,
    "double": 5,
    "apartment": 4,
    "small_suite": 2,
    "medium_suite": 2
}

# Pricing per person
prices = {
    "single": 400,  # Per adult
    "double": 300,  # Per adult
    "apartment_adult": 600,
    "apartment_child": 500,
    "suite_adult": 1000,
    "suite_child": 800
}

# Store customer details
customer_bookings = []

# Function to display available rooms
def display_rooms():
    print(f"Total Number of Rooms available: {sum(rooms.values())}")
    print(f"- Deluxe Single Room: {rooms['single']} rooms left")
    print(f"- Deluxe Double Room (For 2): {rooms['double']} rooms left")
    print(f"  - Per Adult: £{prices['single']} (Single)")
    print(f"  - Per Adult: £{prices['double']} (Double)")
    print(f"- Signature Apartment (Up to 6 people): {rooms['apartment']} rooms left.")
    print(f"  - Per Adult: £{prices['apartment_adult']}")
    print(f"  - Per Child: £{prices['apartment_child']}")
    print("- Presidential Suite (For the recognized ONLY)")
    print(f"  - Small Suite (For 1): {rooms['small_suite']} rooms left")
    print(f"  - Medium Suite (For 2): {rooms['medium_suite']} rooms left")
    print(f"     - Per Adult: £{prices['suite_adult']}")
    print(f"     - Per Child: £{prices['suite_child']}\n")

# Booking process
while True:
    display_rooms()

    # Get user details
    name = input("Enter your name: ")
    adults = int(input("Enter number of adults: "))
    children = int(input("Enter number of children: "))
    total_people = adults + children

    # Choose room
    if total_people == 1:
        room_type = "single"
    elif total_people == 2:
        room_type = "double"
    elif total_people == 3 or total_people == 4:
        print("Available rooms for 3-4 people:")
        print("- Signature Apartment")
        room_type = "apartment"
    elif total_people == 5 or total_people == 6:
        print("Available rooms for 5-6 people:")
        print("- Signature Apartment")
        print("- Presidential Suite (If recognized)")
        choice = input("Enter choice (apartment/suite): ").lower()
        if choice == "suite":
            suite_size = input("Medium Suite only available for 5-6 people. Do you want to proceed? (yes/no): ").lower()
            if suite_size == "yes":
                room_type = "medium_suite"
            else:
                room_type = "apartment"
        else:
            room_type = "apartment"
    else:
        print("Sorry, we do not accommodate more than 6 people in one room.\n")
        continue

    # Check room availability
    if rooms[room_type] > 0:
        # Calculate price
        if room_type in ["single", "double"]:
            total_price = adults * prices[room_type]
        elif room_type == "apartment":
            total_price = (adults * prices["apartment_adult"]) + (children * prices["apartment_child"])
        elif "suite" in room_type:
            total_price = (adults * prices["suite_adult"]) + (children * prices["suite_child"])
        
        # Store booking details
        customer_bookings.append({
            "name": name,
            "room_type": room_type,
            "adults": adults,
            "children": children,
            "total_price": total_price
        })

        # Update room availability
        rooms[room_type] -= 1

        print(f"\nBooking confirmed for {name}!")
        print(f"Room Type: {room_type.replace('_', ' ').title()}")
        print(f"Total Price: £{total_price}\n")

    else:
        print(f"Sorry, {room_type.replace('_', ' ').title()} is fully booked.\n")

    # Continue booking?
    more = input("Do you want to add another booking? (yes/no): ").lower()
    if more != "yes":
        break

# Final Booking Summary
print("\n--- Booking Summary ---")
for booking in customer_bookings:
    print(f"Name: {booking['name']}, Room: {booking['room_type']}, Adults: {booking['adults']}, Children: {booking['children']}, Price: £{booking['total_price']}")
