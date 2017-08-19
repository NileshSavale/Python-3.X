#!/user/bin/python

def add(a,b=10):
    #b is default argument here
    return a+b
	
res=add(100,200)
print (res)
res=add(100)
print(res)