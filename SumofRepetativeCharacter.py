def SumOfRepetativeCharacter(input_string):
    i=0
    
    while i<len(input_string):
        output_string=""
        c=input_string[i]
        count=1
        
        while ((i+1)<len(input_string) and c==input_string[i+1]):
            i=i+1
            count+=1

        output_string+=c
        print (output_string,count)
        i+=1

def main():
    input_string=input("Enter Input String:")
    
    SumOfRepetativeCharacter(input_string)
    
    
if __name__=='__main__':
    main()
