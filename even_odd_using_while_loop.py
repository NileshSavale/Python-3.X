#!/user/bin/python

lb=eval(input("Enter the Lower Bound:"))
ub=eval(input("Enter the Upper Bound:"))

evensum=0
oddsum=0
temp=lb
while lb <= ub:
    if lb%2==0:
	    evensum +=lb
    else:
	    oddsum +=lb
    lb +=1

print ("The Sum of Even numbers from %d to %d is %d" %(temp,ub,evensum))
print ("The Sum of odd Numbers from %d to %d is %d" %(temp,ub,oddsum))