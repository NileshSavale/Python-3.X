#!/user/bin/python


def MaxMin(l):
    max=l[0]
    min=l[0]
    for x in l:
        if x>max:
            max=x
        if x<min:
            min=x
    return max,min
	
def main():
    l=eval(input("Enter the list:"))
    print(MaxMin(l))

if __name__=='__main__':
    main()
