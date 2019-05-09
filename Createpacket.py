def createpacket(crc,length,data,flag):
    packet=crc
    x2=(2**8)-1
    length=length&x2
    packet=packet<<8
    packet=packet|length
    x3=(2**18)-1
    data=data&x3
    packet=packet<<18
    packet=packet|data
    packet=packet<<1
    flag=flag&(1<<1-1)
    packet=packet|flag
    return packet

def main():
    crc=eval(input("Enter crc:"))
    length=eval(input("Enter the length:"))
    data=eval(input("Enter the data:"))
    flag=eval(input("Enter the flag:"))
    output=(createpacket(crc,length,data,flag))
    print("{} is the thirty two bit packet" .format(output))

if __name__=="__main__":
    main()
