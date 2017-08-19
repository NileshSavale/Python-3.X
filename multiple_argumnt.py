#!/user/bin/python

def add(a,b,c=20):
    
    return a+b+c
	
res=add(10,10)
print (res)
res=add(10,b=30)
print (res)
res=add(b=10,a=20)
print (res)
res=add(1,c=200,b=100)
print (res)
res=add(b=30,20)
print  (res)