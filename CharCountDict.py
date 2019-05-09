def charCountDict(input_str):
    result_dict={}
    i=0
    while i<len(input_str):
        if input_str[i] in result_dict:
            result_dict[input_str[i]]=result_dict[input_str[i]]+1
        else:
            result_dict[input_str[i]]=1
        i+=1
    return result_dict

def main():
    input_str=input("Enter the input string:")
    output=charCountDict(input_str)
    print(output)

if __name__=="__main__":
    main()
