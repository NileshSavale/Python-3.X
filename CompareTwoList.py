#!/user/bin/python

def CompareTwoList(L1,L2):
    if type(L1)!= list or type(L2) != list:
        print ("L1 is not list")
        return
    if len(L1)!=len(L2):
        return 0
    L1.sort();L2.sort()
    for i in range(len(L1)):
        if L1[i]==L2[i]:
            continue
        break
    else:
        print("Both List are same")
    return 0
	
def main():
    L1=[eval(input("Enter the First list:"))]
    L2=[eval(input("Enter the First list:"))]
    
    CompareTwoList(L1,L2)
if __name__=='__main__':
    main()

	
