def main():
    name_list = []
    days_list = []
    while True:
        name = input("Enter the name of an employee: ")
        if name == "$":
            break
        else:
            name_list.append(name)
            days = int(input("Enter the number of days absent: "))
            days_list.append(days)

    average = sum(days_list) / len(days_list).round(2)
    print("The average number of days absent per year is: " + str(average))

    max_days = max(days_list)
    max_days_index = days_list.index(max_days)
    print("The name of the person who had the most days of "
          "absence is: " + name_list[max_days_index])

    not_absent = []
    for i in range(len(name_list)):
        if days_list[i] == 0:
            not_absent.append(name_list[i])

    print("The names of the people who were not absent at all "
          "during the year are: " + str(not_absent))

    above_average = []
    for i in range(len(name_list)):
        if days_list[i] > average:
            above_average.append(name_list[i])

    print("The names of the people whose period of absence was above the "
          "average for the year are: " + str(above_average))


main()
