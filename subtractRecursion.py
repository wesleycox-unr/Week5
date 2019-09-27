# subtract 20 to 10

def subtractTo10(num):
    #check if i am in base case
    if num == 10:
        return 0

    return subtractTo10(num-1) + 1
    
print("Number of recursions : {0}".format(subtractTo10(20)))