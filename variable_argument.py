#!/user/bin/python

def variableArgsAdd(*args):
    print(type(args))
    for x in args:
	    print(x)
		
variableArgsAdd(1,2,3)
variableArgsAdd(1,2,3,4,5,6,7,8)