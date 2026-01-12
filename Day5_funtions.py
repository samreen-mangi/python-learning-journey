def ur_name(name):
        #while True:
            if name.lower()=="q":
               print ("program ends")
               #break
            else:
                print("your name is",name)
                #break
while True:
      name1=input("please enter ur name or q if u want to quit")
      ur_name(name1)
      choice = input("Do you want to continue? (y/n): ").strip().lower()
      if choice == "n":
        print("Goodbye.")
        break
