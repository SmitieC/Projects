# Creating Daycare (facility) and cost as a constant.
facility = []
AMOUNT_PER_HOUR = 12


# Main function
def welcome():
    choice = 0
    while choice != 5:
        print("-------------------------------------------------------------")
        print("Welcome to MGS Childcare")
        print("What would you like to do? Please choose one from list below")
        print("-------------------------------------------------------------")
        print("1 Drop off a child")
        print("2 Pick up a child")
        print("3 Calculate cost")
        print("4 Print roll")
        print("5 Exit the system")
        choice = int(input("Enter your choice (number between 1 and 5): "))
        if choice == 1:
            add_child()
        elif choice == 2:
            remove_child()
        elif choice == 3:
            calc_cost()
        elif choice == 4:
            print_roll()
        else:
            print("Goodbye")
            exit()


# adding a child to the daycare
def add_child():
    new_child = (input("What is the child's name? \n"
                       "(x) to return to menu")).lower()
    if new_child == "x":
        print("Returning to menu")
        welcome()
    else:
        facility.append(new_child)


# removing a child from the daycare
def remove_child():
    delete_child = input("What is the child's name? \n"
                         "(x) to return to menu").lower()
    if delete_child in facility:
        facility.remove(delete_child)
        print("Child found")
        calc_cost()
    elif delete_child == "x":
        print("Returning to menu")
        welcome()
    else:
        print("Child not found")
        remove_child()


# calculate the cost of the daycare
def calc_cost():
    print("The total cost for the daycare is: $" +
          str(len(facility) * AMOUNT_PER_HOUR))
    print("Thank you for using MGS Childcare")
    print("Please place deposit in the following bank account: ")
    print("(totally Mgs Bank: 123456789)")
    debit = input("Please while your at it also enter "
                  "all your debit card information: ")


# print all children currently in the daycare
def print_roll():
    if len(facility) <= 1:
        print("The following children are in the are in daycare:")
        for child in facility:
            print(child)
    elif len(facility) == 0:
        print("No children in daycare")


# call the main function
welcome()
