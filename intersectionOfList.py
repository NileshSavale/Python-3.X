#!/user/bin/python
#Accept two list from user and return the intersection of them

def intersectionTwoList(L1,L2):
    L3=[]
    i=0
    j=0
    while i<len(L1):
        while j<len(L2):
		    
            if L1[i]==L2[j]:
                if L1[i] not in L3:
                    L3.append(L1[i])
            j+=1
        if i>=len(L1) and j>=len(L2):
            break		
        i+=1
        j=0
        
    return L3
		
def main():
    L1=eval(input("Enter the First list:"))
    L2=eval(input("Enter the Second list:"))
    
    intersection=intersectionTwoList(L1,L2)
    print (intersection)
    
if __name__=='__main__':
    main()
