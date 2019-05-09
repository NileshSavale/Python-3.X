#! /usr/bin/python

def turnoffRightMostbit(no):
    x=1
    while True:
        if (no&x) !=0:
            return no &(~x)
            break
        x=x<<1

def main():
    no=eval(input("Enter Number to turn off right most bit:"))
    output=turnoffRightMostbit(no)
    print("{} id the number after turning off right most bit of {}" .format(output,no))

if __name__=="__main__":
    main()
