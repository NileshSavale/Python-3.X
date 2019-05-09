#!/user/bin/python

def main():
    file=input("Enter the name of File:")
    fd=open(file)
    line=fd.readline()
    while line !="":
        print(line)
        line=fd.readline()

if __name__=="__main__":
    main()
