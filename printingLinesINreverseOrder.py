# Printing the line in reverse order
def ReverseLineDisplay(fd):
    line=fd.readline()
    while line=="":
        return
    ReverseLineDisplay(fd)
    print(line)

def main():
    file=input("Enter the file Name:")
    fd=open(file)
    ReverseLineDisplay(fd)

if __name__=="__main__":
    main()

    
