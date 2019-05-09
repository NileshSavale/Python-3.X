
def swapSetOfBits(num1,num2,position1,position2,setOfBits):
    if position1>setOfBits and position2>setOfBits:
        x=1<<setOfBits-1
        x1=x<<(position1-setOfBits)
        x2=x<<(position2-setOfBits)
        a=num1&x1
        b=num2&x2
        num1=num1^a
        num2=num2^b
        if position1<position2:
            a=a<<(position2-position1)
            b=b>>(position2-position1)
        else:
            a=a>>(position1-position2)
            b=b<<(position1-position2)
        swap1=num1|b
        swap2=num2|a
    return swap1,swap2

def main():
    num1=eval(input("Enter the first number for swap:"))
    num2=eval(input("Enter the Second number for swap:"))
    position1=eval(input("Enter the first position:"))
    position2=eval(input("Enter the Second position:"))
    setOfBits=eval(input("Enter the set of Bits:"))
    output1,output2=swapSetOfBits(num1,num2,position1,position2,setOfBits)
    print("{} and {} are the number after swap".format(output1,output2))

if __name__=="__main__":
    main()
