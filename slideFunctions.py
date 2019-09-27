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
    
#print("Number of doubling events : {0}".format(doubleTo100(10)))
    
def doubleTo100recursion(num):
    #base case
    if num > 100:
        return 0
    
    
    return doubleTo100recursion(2*num) + 1
    
#print(doubleTo100recursion(10))
    
def fibRecursive(n):
    # fib_n = fib_n-1 + fib_n-2
    
    #base case
    if n < 2:
        return n
    
    return fibRecursive(n-1) + fibRecursive(n-2)
    
# 0 1 1 2 3 5 8 13 21 34 = fib
# 0 1 2 3 4 5 6  7  8  9 = index
#print(fibRecursive(9))

def factorialRecursive(n):
    
    #base case
    if n == 1:
        return 1
    
    return n * factorialRecursive(n-1)
    
inputNumber = 5
print("The factorial of {0} is {1}".format(inputNumber,factorialRecursive(inputNumber)))
   
    
    
    
    