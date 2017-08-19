#!/user/bin/python


# Program: Print below pattern
#   A
#   AB
#   ABC
#   ABCD

def pattern7(no):
    
    for i in range(1,no+1):
        for j in range(65,i+65):
            a=chr(j)
            print ("%c \t" %a,end='')
        print ("\n")
		
def main():
    no=eval(input("Enter Number to for pattern1:"))
    pattern7(no)
	
if __name__=='__main__':
    main()
     
