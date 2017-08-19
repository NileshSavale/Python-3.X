#!/user/bin/python
#WAP :Accept number from user and define a function Sum of cubes of digit


def sumOfCubes (no):
    sum=0
    while no!=0:
        rem=no%10
        sum=(rem*rem*rem)+sum
        no=no//10
    print(sum)
	
def main():
    no=eval(input("Enter Number to obtain Sum of cubes of digit:"))
    sumOfCubes(no)
	
if __name__=='__main__':
    main()	
