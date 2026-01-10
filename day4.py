
def evaluate_students():
    count_pass=0
    count_fail=0
   #while True:
    mark=[]
    for i in range(10):
        marks=int(input("input the marks ten times"))
        mark.append(marks)
    for marks in mark:
        if marks >=50:
            count_pass+=1  
        else:
            count_fail+=1
    return count_pass, count_fail
    print(count_pass,"students are passed")
    print(count_fail,"students are fail")
    #break


while True:
    passed, failed = evaluate_students()
    print(passed, "students are passed")
    print(failed, "students are failed")

    choice = input("Run again? (y/n): ").strip().lower()
    if choice == "n":
        print("Program ended.")
        break
   
   


