#! /user/bin/python

def SumOfRepetativeCharacter(input_string):
    i=0
    output_string=""
    while i<len(input_string):
        c=input_string[i]
        count=1
        while((i+1)<len(input_string) and c==input_string[i+1]):
            i=i+1
            count+=1
        output_string+=c
        output_string+=str(count)
        i+=1
    return output_string

def main():
    input_string=input("Enter the input string:")
    output=SumOfRepetativeCharacter(input_string)
    print(output)

if __name__=='__main__':
    main()
