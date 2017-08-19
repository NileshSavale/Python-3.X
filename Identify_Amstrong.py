#!/user/bin/python
#WAP :To accept a number from user and check if it is amstrong number


def identifyAmstrong (no):
    sum=0
    temp=no
    while no!=0:
        rem=no%10
        sum=(rem*rem*rem)+sum
        no=no//10
    print(sum)
    if sum == temp:
        print("The given Number is Amstrong")
    else:
        print ("The given Number is not Amstrong")
	
def main():
    no=eval(input("Enter Number to obtain Sum of cubes of digit:"))
    identifyAmstrong(no)
	
if __name__=='__main__':
    main()
