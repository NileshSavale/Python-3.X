#!/user/bin/python
while 1:
    rating=eval(input ("Enter the Rating :"))

    if rating == 5:
	    print ("Performance is Exceptional")
    elif rating == 4:
        print ("Performance is Excellent")
    elif rating == 3:
	    print ("Performance is Very good")
    elif rating == 2:
	    print ("Performance is Good")
    elif rating == 1:
	    print ("Performance is poor")
    else:
        print ("Please Enter Valid Rating")
