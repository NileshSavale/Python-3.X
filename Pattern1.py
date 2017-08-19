#!/user/bin/python

# Program: Print below pattern
#   *
#   **
#   ***
#   ****

def pattern1(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print ('*\t',end='')
        print ("\n")
		
def main():
    no=eval(input("Enter Number to for pattern1:"))
    pattern1(no)
	
if __name__=='__main__':
    main()
    
