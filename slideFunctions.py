# create functions for each slide


def doubleThisNow(num):
    result = 2*num
    print(result)

#doubleThisNow(5)    
   
def doubleThisGive(num):
    return 2*num

#doubled = doubleThisGive(5)
#print(doubled)

def multiplyThese(a, b):
    print(a)
    print(b)
    print("First number is {0} and second is {1}".format(a, b))
    print(str(a) + " " + str(b))
    
    return a*b

#print("Result of product is : " + str(multiplyThese(3,5)))

def isFrance(word):
    if word == "France":
        print("Oui")
        return True
#    if word != "France":
    else:
        print("Non monsieur")
        return False
#    return word == "Frace"
   
#print("The result is : " + str(isFrance("Germany")))
    
def xTimes2y(a, b):
    return a * doubleThisGive(b)

#print("The result is : {0}".format(xTimes2y(3,9 )))
    
def doubleTo100(num):
    # Return how many times the input is doubled
    # to exceed 100
    doubledValue = num
    n = 0
    
    while doubledValue <= 100:
        # do something
        n += 1
        
        doubledValue = doubledValue * 2
    
    return n
    
print("Number of doubling events : {0}".format(doubleTo100(10)))
    
    
    
    
    
    
    
    
    
    
    
    
    