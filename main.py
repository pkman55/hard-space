import disk_space

yesno = "Yes"
while yesno == "Yes":
    print("Hello :)\n")
    print("If you would like to know the total space enter: Total")
    print("If you would like to know the used space enter: Used")
    print("If you would like to know the free space enter: Free\n")
    answer = input()

    while answer != "Total" and answer != "Used" and answer != "Free":
        print("Invalid input try again\n")
        answer = input()


    if answer == "Total":
        disk_space.Total_Space()
    elif answer == "Used":
        disk_space.Used_Space()
    elif answer == "Free":
        disk_space.Free_Space()
    else:
        print("Invalid output")
    print("If you would like to go again enter: Yes\n")
    print("If not: No\n")
    yesno = input()

    while yesno != "Yes" and yesno != "No":
        print("Invalid input try again\n")
        yesno = input()
