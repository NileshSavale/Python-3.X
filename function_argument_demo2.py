#!/user/bin/python
#this program will not work because default argumet should be trailing 
def add(a=10,b):
    #b is default argument here
    return a-b
	
res=add(100)
print (res)