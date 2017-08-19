#!/user/bin/python
#WAP: accept list from user and an element whose present /occurence needs to be counted

def countOccurance (l,key):
    count=0
    for x in l:
        print (x)
        if key==x:
            count +=1
    return count

def main():
    l=[eval(input("Enter the list:"))]
    Key=eval(input("Enter Number for which Occurance need to count:"))
    print (countOccurance(l,Key))
	
if __name__=='__main__':
    main()
