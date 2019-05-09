#! /usr/bin/python

def CountBit(no):
    count=0
    x=1
    while x<=no:
        if (no & x)!=0:
            count +=1
        x=x<<1
    return count

def main():
    no=eval(input("Enter Number to count number of Bits:"))
    output=CountBit(no)
    print("{} Number of one bits in {}" .format(output,no))


if __name__=="__main__":
    main()
