#!/user/bin/python

#pattern 3:
#    *
#   **
#  ***
# ****
#*****


def pattern3(no):
    for i in range(1,no+1):
        for j in range (1,no-i+1):
            print('\t',end='')
        for j in range (1,i+1):
            print ('*\t',end='')
        print ("\n")
	
def main():
    no=eval(input("Enter Number to for pattern2:"))
    pattern3(no)
	
if __name__=='__main__':
    main()
