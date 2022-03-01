def routine():
    total_fines = 0
    amount_fines = 0
    speeder_list = []
    speed_list = []
    run_new = input("would you like to enter a new speeder? (y/n):")
    while run_new != "n":
        name = input("Enter first and last name of speeder: ").capitalize()
        speed = int(input("Enter the amount over speed limit: "))
        if name == "James Wilson" or name == \
                "Helga Norman" or name == "Zachary Conroy":
            print(name, " - WARRANT TO ARREST")
        if speed < 10:
            print(name, "to be fined $30")
            amount_fines += 30
        elif 10 <= speed < 15:
            print(name, "to be fined $80")
            amount_fines += 80
        elif 15 <= speed < 20:
            print(name, "to be fined $120")
            amount_fines += 120
        elif 20 <= speed < 25:
            print(name, "to be fined $170")
            amount_fines += 170
        elif 25 <= speed < 30:
            print(name, "to be fined $230")
            amount_fines += 230
        elif 30 <= speed < 35:
            print(name, "to be fined $300")
            amount_fines += 300
        elif 35 <= speed < 40:
            print(name, "to be fined $400")
            amount_fines += 400
        elif 40 <= speed < 45:
            print(name, "to be fined $510")
            amount_fines += 510
        elif speed >= 45:
            print(name, "to be fined $630")
            amount_fines += 630
        total_fines += 1
        speeder_list.append(name)
        speed_list.append(speed)
        run_new = input("would you like to enter a new speeder? (y/n)")
    else:
        print("Today's Summary:")
        print("Total fines:", total_fines)
        for i in range(total_fines):
            print(i + 1, ") Name:", speeder_list[i],
                  "Amount Over Limit:", speed_list[i])
        print("Total amount of fines: $", amount_fines)
        print("Goodbye!")
        exit()


# main
print("Good Morning!")
routine()
