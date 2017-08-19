#!/user/bin/python

def reverse(l):
    length=len(l)
    i=0
    j=length-1
    m=[]
    while i<length:
        print (m)
        m.append(l[j])
        print (m)
        i+=1
        j-=1
    return m
	
def main():
    l=eval(input("Enter the list:"))
    rev_list=reverse(l)
    print (rev_list)

if __name__=='__main__':
    main()
