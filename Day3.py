#print ("Day 3 is started n i m so excite and getting this done")
count_pass=0
count_fail=0
while True:
    mark=[]
    for i in range(10):
        marks=int(input("input the marks ten times"))
        mark.append(marks)
    for marks in mark:
        if marks >=50:
            count_pass+=1                 
        else:
            count_fail+=1
    print(count_pass,"students are passed")
    print(count_fail,"students are fail")
    break
    




    

