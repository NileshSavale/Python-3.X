#WAP: to accept a number ,position and number of bits to be turned off from given position . Turn off specified bits from number.

def turnOffSetOffBits(no,position,setOfBits):
    if position>setOfBits:
        x=1<<setOfBits-1
        x=x<<(position-setOfBits)
        return no&(~x)

    return -1

def main():
    no=eval(input("Enter the number to turn off the bits:")
    position=eval(input("Enter the position:"))
    setOfBits=eval(input("Enter the set of Bits:"))
    output=turnOffSetOffBits(no,position,setOfBits)
    print("{} is the number afrer turning off right most bit of {}".format(output,no))

if __name__=="__main__":
    main()
