todo_list = ["eat", "sleep", "bath"]
while True:
    print("--TO DO LIST--")
    print("1. Inspect TO DO LIST")
    print("2. Add TO DO LIST")
    print("3. Remove TO DO LIST")
    print("4. Exit")
    start= int(input("Choose Option "))
    if start == 1:
        for index, tugas in enumerate(todo_list, start=1):
            print(f"{index}. {tugas}")

    elif start == 2:
        print ("Insert new list ")
        new = input()
        todo_list.append(new)
    elif start == 3:
        print(todo_list)
        print("Choose to Remove ")
        rmv = input()
        todo_list.remove(rmv)
    elif start == 4:
        print("--Done--")
        break
