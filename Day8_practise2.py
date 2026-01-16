def handle_choice(choice):
    if choice.lower()=="a":
        print("this is the name", choice)
    else:
        print("this is the age ", choice)
    
while True:
    choice1=input("please enter your choice")
    if choice1=="q":
         print("exit")
         break 
    handle_choice(choice1)

           
