def InsertEDetails(Dict):
    if any(Dict)==False:
        num=eval(input("Enter the Number of Employee for which list has to create"))
        for x in range(1,num+1):
            emp={}
            emp["Name"]=input("Emter the name of Employee:")
            emp["DOB"]=input("Enter the DOB:")
            emp["Address"]=input("Enter the address:")
            emp["Salary"]=input("Enter the Salary:")
            Dict[x]=emp
    else:
        emp={}
        emp["Name"]=input("Enter the name of Employee:")
        emp["DOB"]=input("Enter the DOB:")
        emp["Address"]=input("Enter the Address:")
        emp["Salary"]=input("Enter the Salary:")
        Dict[(max(Dict.keys())+1)]=emp
    print(Dict)

def UpdateEDetails(Dict,Emp_Id):
    print("Please Enter what details you want to update for below Emplyee:")
    print(Dict[Emp_ID])
    detail=input("Enter the Details:")
    Dict[Emp_Id][details]=input("Enter the value:")

def DeleteEDetails(Dict,Emp_Id):
    del Dict[Emp_Id]
    print(Dict)

def Display(Dict):
    print(Dict)

def SearchEDetails(Dict,Emp_Id):
    print("Employee Details are as below")
    print(Dict[Emp_Id])

def menu():
    while True:
        print("*****#Welcome to TCS Employee Journal#*****")
        print("You can perform following operations")
        print("1.Create Employee list\n2.Insert Employee Details\n3.Update Employee Details\n4.Remove Employee from list\n5.Display Empolyee List\n6.Search Employee\n7.Exit")
        choice=eval(input("Enter your Choice:"))
        if choice<=7:
            return choice
            break
    
def main():
    Dict={}
    choice=menu()
    print(choice)
    while choice !=8:
        if choice==1:
            InsertEDetails(Dict)
            choice=menu()
        elif choice==2:
            InsertEDetails(Dict)
            choice=menu()
        elif choice==3:
            Emp_Id=eval(input("Enter the Emp_Id for which details need to update:"))
            UpdateEDetails(Dict,Emp_Id)
            choice=menu()
        elif choice==4:
            Emp_Id=eval(input("Enter the Emp_Id which need to delete:"))
            DeleteEDetails(Dict,Emp_Id)
            choice=menu()
        elif choice==5:
            Display(Dict)
            choice=menu()
        elif choice==6:
            Emp_Id=eval(input("Enter the Emp_Id which need to search:"))
            SearchEDetails(Dict,Emp_Id)
            choice=menu()
        elif choice==7:
            print("Exiting Application")
            break
        else:
            choice=menu()
			
if __name__=="__main__":
    main()
			
		
            
