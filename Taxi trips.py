def main():
    driver_name = str(input("What is your name? "))
    print("Hello " + driver_name + "!")
    while True:
        start_trip = input("Would you like to start a new trip? (yes/no) ")
        if start_trip == "yes":
            trip_time = int(input("How long did the trip take? (minutes) "))
            trip_cost = 10 + (trip_time * 2)
            print("Your trip cost is $" + str(trip_cost))
        else:
            break
    print("Thank you for using the taxi service!")
    print("{} Well done today!".format(driver_name))
    print("Total time of all trips: " + str(trip_time))
    print("Average time of all trips: " + str(trip_time / 2))
    print("Total income for the day: $" + str(trip_cost))
    print("Average cost of all trips: $" + str(trip_cost / 2))


main()
