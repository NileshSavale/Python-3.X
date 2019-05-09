def long_short_line(file):
    fd=open(file)
    line=fd.readline()
    input_str=str(line)
    long_line_length=len(input_str)
    short_line_length=len(input_str)
    long_str=""
    short_str=""
    while line !="":
        input_str=str(line)
        if (len(input_str)>long_line_length):
            long_line_length=len(input_str)
            long_str=input_str
        if (len(input_str)<short_line_length):
            short_line_length=len(input_str)
            print(short_str)
            short_str=input_str
        line=fd.readline()
    return long_line_length,long_str,short_line_length,short_str

def main():
    file=input("Enter the name of File:")
    long_line_length,long_str,short_line_length,short_str=long_short_line(file)
    print("Long line length is :{}".format(long_line_length))
    print("Long line is : {}".format(long_str))
    print("Short line length is: {}".format(short_line_length))
    print("Short line is :{}".format(short_str))

if __name__=="__main__":
    main()

    
