#!/user/bin/python

n=eval(input("Enter the Value:"))
sum=0

for x in range(2,n+1,2):
    sum +=x
print("Sum of even number upto %d is %d"%(n,sum))