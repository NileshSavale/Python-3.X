#!/user/bin/python

def pattern1(no):
    c=65
    for i in range(1,no+1):
        for j in range(c,c+1):
            print ("%ch",%c)
        print ("\n")
		
def main():
    no=eval(input("Enter Number to for pattern1:"))
    pattern1(no)
	
if __name__=='__main__':
    main()
