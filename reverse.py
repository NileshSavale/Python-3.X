#!/user/bin/python

#Program:Accept number from user and reverse it 

def rervNum (no):
    rev=0
    while no!=0:
        rem=no%10
        rev=rev*10+rem
        no=no//10
    print(rev)
	
def main():
    no=eval(input("Enter Numberto rervse:"))
    rervNum(no)
	
if __name__=='__main__':
    main()
		
	
