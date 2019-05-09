
def Depakatize(packet):
    flag=packet&((1<<1)-1)
    packet=packet>>1
    data=packet&((1<<18)-1)
    packet=packet>>18
    length=packet&((1<<8)-1)
    packet=packet>>8
    crc=packet&((1<<5)-1)
    return crc,lenght,data,flag

def main():
    packet=eval(input("Enter the packet:"))
    crc,lenght,data,flag=Depacketize(packet)
    print("crc={} \nlenght= {}\ndata= {}\nflag= {}".format(crc,length,data,flag))

if __name__=="__main__":
    main()
    
