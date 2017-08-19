#!/user/bin/python

# Program:accept two numbers from number and find GCD of them

def GCD(no1,no2):
    
    while no1!=no2:
	    if (no1>no2):
		    no1=no1-no2
	    else:
		    no2=no2-no1
    print(no1)
	
def main():
    no1=eval(input("Enter First Number:"))
    no2=eval(input("Enter Second Number:"))
    GCD(no1,no2)

if __name__=='__main__':
    main()
    
