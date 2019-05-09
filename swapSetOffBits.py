
def swapSetOffBits(num1,num2,position,setOfBits):
    if position>setOfBits:
        x=(1<<setOfBits)-1
        x=x<<(position-setOfBits)
        a=num1&x
        b=num2&x
        num1=num1^a
        num2=num2^b
        swap1=num1|b
        swap2=num2|a
    return swap1,swap2

def main():
    num1=eval(input("Enter the first number to swap:"))
    num2=eval(input("Enter the Second number to swap"))
    position=eval(input("Enter the position:"))
    setOfBits=eval(input("Enter the set Of Bits:"))
    output1,output2=swapSetOffBits(num1,num2,position,setOfBits)
    print("{} and {} are the number after swapping {} number of Bits at {} position of {} and {} ".format(output1,output2,setOfBits,position,num1,num2))

if __name__=="__main__":
    main()
