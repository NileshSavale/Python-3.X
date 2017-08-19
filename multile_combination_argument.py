#!/user/bin/python

def add_multi (a,b=0,c=0,d=0,e=10):
    print(a,b,c,d,e)
    return a+b+c+d+e
	
res=add_multi(5,6,6)
print(res)

res=add_multi(10,b=10,e=30,d=50)
print(res)

res=add_multi(50,20,d=50)
print(res)

res=add_multi(c=50,20,d=50)#SyntaxError: positional argument follows keyword argument
print(res)

