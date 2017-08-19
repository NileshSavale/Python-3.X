#!/user/bin/python

def mergeTwoList(L1,L2):
    L3=[]
    i=0
    j=0
    while i<len(L1) and j<len(L2):
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i+=1
        else:
            L3.append(L2[j])
            j+=1
    if i<len(L1):
        L3.extend(L1[i:])
    if j<len(L2):
        L3.extend(L2[j:])
    return L3
		
def main():
    L1=eval(input("Enter the First list:"))
    L2=eval(input("Enter the First list:"))
    
    Merged_List=mergeTwoList(L1,L2)
    print (Merged_List)
if __name__=='__main__':
    main()
