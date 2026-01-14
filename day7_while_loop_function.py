def ur_name(choice):
    if choice=="a":
            name1=input("Enter ur name")
            print(name1)
    else:
        print("your choice is other than A")


while True:
    choice1=input("please enter your choice either A or q to exit").strip().lower()
    if choice1== "q":
        print("program ended")
        break
    ur_name(choice1)

        

