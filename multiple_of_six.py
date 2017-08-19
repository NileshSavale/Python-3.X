#!/user/bin/python

startv=eval(input ("Enter the start value:"))
endv=eval(input("Enter the end value:"))
sum=0 

for i in range (startv,endv):
    if i % 6==0:
	    sum +=i
	    print ("Sum is %d" %sum)
	    continue

print ("The sum of multiple of 6 is %d" %sum)

