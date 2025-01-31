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
    chosen = apartment


           
