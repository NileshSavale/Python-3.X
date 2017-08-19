#!/user/bin/python

# Program :Palindrom 

def palinedrom(no):
    no1=no
    rev=rervNum (no)
    if rev==no1:
	    print("Given Number is palindrom")
	
def main():
    no=eval(input("Enter Number to rervse:"))
    palinedrom(no)

if __name__=='__main__':
    main()
    