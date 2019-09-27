# sum two numbers and print them

import sys

# arguments live in sys.argv

#sys.argv = ["sumTwoNumbers.py", 3, 5]


if len(sys.argv) != 3:
    print("Usage: python " + sys.argv[0] + " <first number> <second number>")
    sys.exit()

first = int(sys.argv[1])
second = int(sys.argv[2])

print("{0} and {1}".format(first,second))


#result = first + second
#print(result)
    
    
def addTheseTogether(a, b):
    #when im in here
    
    result = a + b
    return result
    
    
addedTogether = addTheseTogether(first, second)
print(addedTogether)
    