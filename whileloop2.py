#!/user/bin/python

n=eval(input("Enter value of n"))

sum=0
i=1

while i<=n:
    if i%2==0:
        sum+=i
	i+=1
print ("Sum of even numbers from 1 to %d is %d"%(n,sum))