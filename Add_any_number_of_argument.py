#!/user/bin/python

def variableArgsAdd(*args):
    sum=0
    print(type(args))
    for x in args:
	    sum+=x
	    
    print(sum)
	
variableArgsAdd(10,20,30,40,50,60,70)
variableArgsAdd(1,2,3,4,5,6,7,8)