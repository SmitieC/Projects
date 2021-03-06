# You will be designing basic software for a booking system for the local University's vehicle
# booking system. It allows staff to borrow a vehicle for the day, and keeps track of which vehicles
# have already been booked.
# Specifications:
# ● The program will be started at the beginning of each day, and closed at the end of the
# day.
# ● All vehicles are available at the start of the day.
# ● The following vehicles can be hired:
# Car Number Car Type Number of Seats
# 1 Suzuki Van 2
# 2 Toyota Corolla 4
# 3 Honda CRV 4
# 4 Suzuki Swift 4
# 5 Mitsubishi Airtrek 4
# 6 Nissan DC Ute 4
# 7 Toyota Previa 7
# 8 Toyota Hi Ace 12
# 9 Toyota Hi Ace 12
# ● The program should:
# 1. Ask the user for the number of seats needed in the vehicle.
# 2. Display all available vehicles to be booked.
# 3. If a vehicle doesn't have enough seats, it should have a note beside the vehicle
# stating this (for example: "Not enough seats")
# 4. Ask the user for the number of the vehicle to be booked.
# 5. If the vehicle is available, the program should also keep track of the name of the
# person who booked the vehicle.
# ● The program should stop the input mode when no more vehicles are available for hire,
# or when the user types in -1 for the number of seats as a signal to stop input mode.
# The user should also be told they can do this.
# ● At the end of the day when the input mode is stopped, the following information should
# be displayed for all vehicles booked on that day:
# 1. Vehicle number
# 2. Vehicle type
# 3. Name of person who booked vehicle

cars = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    print("Welcome to the University's Vehicle Booking System")
    name = input("Please enter your name: ")
    print("Please enter the number of seats you need:")
    seats = int(input())
    if seats == -1:
        print("Thank you for using the University's Vehicle Booking System")
        return "none"
    print(
        "Because of the amount of seats you have requested, "
        "we have the following vehicles available for you:")
    if seats <= 2 and 1 in cars:
        print("1. Suzuki Van")
    elif seats <= 4 and 2 in cars:
        print("2. Toyota Corolla")
    if seats <= 4 and 3 in cars:
        print("3. Honda CRV")
    if seats <= 4 and 4 in cars:
        print("4. Suzuki Swift")
    if seats <= 4 and 5 in cars:
        print("5. Mitsibishi Airtrek")
    if seats <= 4 and 6 in cars:
        print("6. Nissan DC Ute")
    if seats <= 7 and 7 in cars:
        print("7. Toyota Previa")
    if seats <= 12 and 8 in cars:
        print("8. Toyota Hi Ace")
    if seats <= 12 and 9 in cars:
        print("9. Toyota Hi Ace")
    else:
        print("Sorry, we do not have any vehicles available for you")
        return "none"
    print("Please enter the number of the vehicle you would like to book:")
    vehicle = int(input())
    if vehicle == 1:
        print("Thank you for booking the Suzuki Van")
        names.pop(0)
        names.insert(0, name)
        cars.pop("1")
    if vehicle == 2:
        print("Thank you for booking the Toyota Corolla")
        names.pop(1)
        names.insert(1, name)
        cars.pop("2")
    if vehicle == 3:
        print("Thank you for booking the Honda CRV")
        names.pop(2)
        names.insert(2, name)
        cars.pop("3")
    if vehicle == 4:
        print("Thank you for booking the Suzuki Swift")
        names.pop(3)
        names.insert(3, name)
        cars.pop("4")
    if vehicle == 5:
        print("Thank you for booking the Mitsubishi Airtrek")
        names.pop(4)
        names.insert(4, name)
        cars.pop("5")
    if vehicle == 6:
        print("Thank you for booking the Nissan DC Ute")
        names.pop(5)
        names.insert(5, name)
        cars.pop("6")
    if vehicle == 7:
        print("Thank you for booking the Toyota Previa")
        names.pop(6)
        names.insert(6, name)
        cars.pop("7")
    if vehicle == 8:
        print("Thank you for booking the Toyota Hi Ace")
        names.pop(7)
        names.insert(7, name)
        cars.pop("8")
    if vehicle == 9:
        print("Thank you for booking the Toyota Hi Ace")
        names.pop(8)
        names.insert(8, name)
        cars.pop("9")
    else:
        print("Sorry, we do not have any vehicles by that number")
        return "error"


if main() == "none":
    print("")
