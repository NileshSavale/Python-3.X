#!/user/bin/python

#pattern 5:
#   *
#  **
# ***
#****
#****
# ***
#  **
#   *



def pattern4(no):
    for i in range(1,no+1):
        for j in range (1,no-i+1):
            print('\t',end='')
        for k in range (1,i+1):
            print ('*\t',end='')
        print ("\n")
    for i in range(1,no+1):
        for j in range (1,i):
            print('\t',end='')
        for k in range (1,no-i+2):
            print ('*\t',end='')
        print ("\n")
def main():
    no=eval(input("Enter Number to for pattern2:"))
    pattern4(no)
	
if __name__=='__main__':
    main()
