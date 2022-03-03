seats = 0
cars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
name = []
print("Welcome to the Vehicle Booking System")


def choose():
    global seats
    while seats != "-1":
        seats = int(input("Please enter the number of seats you need: "))
        print("Please select a vehicle")
        if "1" in cars and seats <= 2:
            print("1. Suzuki Van")
        if "2" in cars and seats <= 4:
            print("2. Toyota Corolla")
        if "3" in cars and seats <= 4:
            print("3. Honda CRV")
        if "4" in cars and seats <= 4:
            print("4. Suzuki Swift")
        if "5" in cars and seats <= 4:
            print("5. Mitsubishi Airtrek")
        if "6" in cars and seats <= 4:
            print("6. Nissan DC Ute")
        if "7" in cars and seats <= 7:
            print("7. Toyota Previa")
        if "8" in cars and seats <= 12:
            print("8. Toyota Hi Ace")
        if "9" in cars and seats <= 12:
            print("9. Toyota Hi Ace")
        else:
            print("Sorry, we don't have enough seats for you")
            print("Please enter -1 to exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            print("You have booked a Suzuki Van")
            cars.remove("1")
            return "1"
        elif choice == 2:
            print("You have booked a Toyota Corolla")
            cars.remove("2")
            return "2"
        elif choice == 3:
            print("You have booked a Honda CRV")
            cars.remove("3")
            return "3"
        elif choice == 4:
            print("You have booked a Suzuki Swift")
            cars.remove("4")
            return "4"
        elif choice == 5:
            print("You have booked a Mitsubishi Airtrek")
            cars.remove("5")
            return "5"
        elif choice == 6:
            print("You have booked a Nissan DC Ute")
            cars.remove("6")
            return "6"
        elif choice == 7:
            print("You have booked a Toyota Previa")
            cars.remove("7")
            return "7"
        elif choice == 8:
            print("You have booked a Toyota Hi Ace")
            cars.remove("8")
            return "8"
        elif choice == 9:
            print("You have booked a Toyota Hi Ace")
            cars.remove("9")
            return "9"
        else:
            print("You have entered an invalid choice")
            print("Please enter -1 to exit")
    return "exit"


while choose() != "exit":
    name.append(input("Please enter your name: "))
print("Vehicles Booked")
for i in range(len(cars)):
    print(cars[i])
print("Names who booked the vehicles")
for i in range(len(name)):
    print(name[i])
print("Thank you for using the Vehicle Booking System")
