#!/user/bin/python


a=eval(input("Enter Number:"))
b=eval(input("Enter Number:"))
c=eval(input("Enter Number:"))

if a<b and a<c:
    print("%d is smaller" %a)
	
elif b<c:
    print ("%d is smaller" %b)
	
else:
    print ("%d is smaller" %c)