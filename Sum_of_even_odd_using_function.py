#!/user/bin/python

def SumOfEvenOdd(lb,ub)

    evensum=0
    oddsum=0

    while lb <= ub:
        if lb%2==0:
	        evensum +=lb
        else:
	        oddsum +=lb
    lb +=1
	
    return evensum,oddsum

if __name__=='__main__':
    lb=eval(input("Enter the Lower Bound:"))
    ub=eval(input("Enter the Upper Bound:"))
	r1,r2=SumOfEvenOdd(lb,ub)
	print(r1,r2)