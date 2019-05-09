# Petrol Prices

def CalCulateAvgPetrolPrices(file):
    fd=open(file)
    line=fd.readline()
    Sum_Mha=0
    Sum_Goa=0
    Sum_Ka=0
    Count=0
    while (line != ""):
        input_str=str(line)
        input_str=input_str.split(" ")
        Sum_Mha+=int(input_str[2])
        Sum_Goa+=int(input_str[3])
        Sum_Ka+=int(input_str[4])
        Count+=1
        line=fd.readline()
    Avg_Mha=Sum_Mha/Count
    Avg_Goa=Sum_Goa/Count
    Avg_Ka=Sum_Ka/Count
    return Avg_Mha,Avg_Goa,Avg_Ka

def main():
    file=input("Enter the file which contain the petrol prices:")
    Avg_Mha,Avg_Goa,Avg_Ka=CalCulateAvgPetrolPrices(file)
    f=open("E:\Python Material\Input_Files_to_rogram\Petrol_avg_out.txt",'w')
    f.write('Maharashtra Average Petrol Prices:{}\n'.format(Avg_Mha))
    f.write('Goa Average Petrol Prices:{}\n'.format(Avg_Goa))
    f.write('Karnataka Avarage Petrol Prices:{}'.format(Avg_Ka))
    f.close()

if __name__=="__main__":
    main()

    
