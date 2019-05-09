#WAP :to take file input from user and create the dictonary and put into that

def create_dict_from_file (file):
    dict={}
    fd=open(file)
    line=fd.readline()
    while line !="":
        input_str=str(line)
        if input_str.startswith('#') or input_str.startswith('[') or input_str.startswith('\n'):
            line=fd.readline()
            continue
        else:
            split_line=input_str.split('=')

            if '#' in split_line[1]:
                split_line[1]=split_line[1].split('#')[0]
            if '\n' in split_line[1]:
                split_line[1]=split_line[1].split('\n')[0]
            dict[split_line[0]]=split_line[1]
        line=fd.readline()
        print(dict)
    return dict

def main():
    file=input("Enter the File Name:")
    output=create_dict_from_file(file)
    print(output)

if __name__=="__main__":
    main()
