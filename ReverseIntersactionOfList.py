#!/user/bin/python

#WAP 3:inverse the intersaction 


def RintersectionTwoList(L1,L2):
    L3=[]
    i=0
    j=0
    L4=[]
    while i<len(L1):
        while j<len(L2):
		    
            if L1[i]==L2[j]:
                if L1[i] not in L3:
                    L3.append(L1[i])
            else :
                if L1[i] not in L4:
                    L4.append(L1[i])
                if L2[j] not in L4:
                    L4.append(L2[j])	
            j+=1
        if i>=len(L1) and j>=len(L2):
            break		
        i+=1
        j=0
        
    return L4
		
def main():
    L1=eval(input("Enter the First list:"))
    L2=eval(input("Enter the Second list:"))
    
    intersection=RintersectionTwoList(L1,L2)
    print (intersection)
    
if __name__=='__main__':
    main()
