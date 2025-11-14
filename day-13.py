
print("Wecome to Grud steyem...")
print()
print()
students=[]
uid = 1
while True: 


    print(" 🔍press 1 for  add student")
    print(" 🔍 press 2 for  view student")
    print(" 🔍 press 3 for add age student")
    print(" 🔍 press 4 for add course student")
    print(" 🔍 press 5 for add remove student")
    print(" 🔍 press 6 for add exit student")
    print()
    print()

    choice = int(input("Enter your choice (1/5)🔍🔍🔍:"))
    

    if (choice==1):
        Name=input("Enter your name-:")
        age= int(input("Enter your age-:"))
        course= input("Enter your course-:")
        st={"uid":uid,
        "Name":Name,
        "age":age, 
        "course":course}
        students.append(st)
        uid = uid+1

    elif(choice==2):
        print("Id  |  Name  | Age  | course  |")
        for st in students:
            print(f"{st["uid"]}    {st["Name"]}  | {st["age"]}      |  {st["course"]}")

       
    elif(choice==3):

        usid=int(input("Enter your age of students "))
        for st in students:
            if (st["uid"] == usid):
                st["age"]=int(input("Enetr your age"))
                break
            
            print("edit student of successfully")


    elif(choice==4):

        usid=int(input("Enter your course of students "))
        for st in students:
            if (st["uid"] == usid):
                st["age"]=(input("Enetr your course"))
                break
            
            print("edit student of successfully")


        

    elif(choice==5):
       

        sid=int(input("Enter remove student  "))
        for st in students:
            if st["uid"] == sid:
                students.remove(st)
                print(" Student removed successfully")
        
        else:
            print(' student not found')
            

    
       
    elif(choice==6):
        print("exit....................")
        break
    else:
        ("Enter your vaild number")
        

    



    




