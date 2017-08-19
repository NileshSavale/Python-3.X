#!/user/bin/python

#Pattern 2:
#*****  1
#****
#**
#*

def pattern2(no):
    for i in range(1,no+1):
        for j in range (1,no-i+2):
            print('*\t',end='')
        print ("\n")
	
def main():
    no=eval(input("Enter Number to for pattern2:"))
    pattern2(no)
	
if __name__=='__main__':
    main()
