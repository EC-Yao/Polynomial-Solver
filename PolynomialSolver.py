import math
import sys

x = 0 # Gets the degree of the polynomial from the user
y = 0 # Gets the coefficients of the polynomial from the user (uses a for loop)
coefficients = [] # Essentially stores the original polynomial
templist = [] # Temporary list to find all factors of a constant
possrootsn = [] # Possible roots of the first coefficient (see Rational Roots Test)
possroots0 = [] # Possible roots of the last coefficient (see Rational Roots Test)
possroots = [] # Lists all possible roots (Rational Roots Test)
tempcoefficients = [] # Helps count the number of possible positive roots (Descartes Rule of Sign)
negcoefficients = [] # Used to calculate possible number of negative roots (Descartes Rule of Sign)
numposroots = 0 # Number of possible positive roots (Descartes Rule of Sign)
numnegroots = 0 # Number of possible negative roots (Descartes Rule of Sign)
found = False # Checks to see if the remaining polynomial is factorable or not
temproot = 0 # Helps check to see whether the remaining polynomial is factorable or not
totalposroots = [] # Total number of positive roots
totalnegroots = [] # Total number of negative roots
finalpoly = [] # Final polynomial in coefficients (computer-friendly)
firstoutput = '' # Returns the input polynomial in a user-friendly format
finaloutput = '' # Returns the final output in a user-friendly format

def synthdiv(dividend, divisor): # Synthetically divides a list of coefficients by another one (converts list into polynomial)
    divis = list(dividend)
    divid = divisor[0]
    for a in range(len(dividend)-(len(divisor)-1)): # Synthetically divides the coefficients based on the degree of each polynomial
        divis[a] /= divid 
        coef = divis[a]
        if coef != 0:
            for b in range(1, len(divisor)): # Actual process doing the synthetic addition and making another list of coefficients
                divis[a + b] += -divisor[b] * coef
    separator = -(len(divisor)-1) # Sets a variable to cut the final result into the answer and the remainder
    if divis[separator:] == [0.0]: # If the remainder is 0, return the answer, otherwise return 0 (easy to program for other functions)
        return divis[:separator]
    else:
        return 0

def factors(x): # Finds and returns all factors of a constant
    global templist
    templist = []
    for a in range(1,int(math.floor(math.sqrt(x))+1)): # Goes through all numbers between 1 and the square root of the number
        if x%a == 0: # Checks to see if the number is a factor, if it is, then add the number and the constant divided by the number
            templist.append(a)
            templist.append(int(x/a))
    if math.sqrt(x)%1 == 0: # Removes the square root of the number if the square root is an integer (Since the square root would then have been added twice)
        templist.remove(math.sqrt(x))
    templist.sort()
    return templist # Returns the list of factors, sorted

print("""
This is a polynomial factoring code
Eddy Yao, January 5, 2016
We don't accept fraction coefficients, sorry!
""")

x = int(input('How many terms are in your equation? (Include powers with 0 coefficient)')) # Gathers the degree of the polynomial
if x < 1 or x%1 != 0:
    print('Nice try')
    sys.exit()
y = int(input('What is the coefficient of the highest power? (Include powers with 0 coefficient)')) # Collects coefficients from the user
coefficients.append(y) # Adds the collected information to a list
negcoefficients.append(y) #  See line 57
tempcoefficients.append(y) # See line 57

for a in range(0,x-1): # Essentially executes lines 55-59 until the entire polynomial has been input
    y = int(input('What is the coefficient of the next highest power? (Include powers with 0 coefficient)'))
    coefficients.append(y)
    negcoefficients.append(y)
    tempcoefficients.append(y)

for b in range(0,len(coefficients)): # Creates a user-friendly version of the polynomial
    if coefficients[b] != 0: # If the coefficient isn't 0, go on, otherwise skip it and move to the next coefficient
        if coefficients[b] > 0 and b != 0: # Adds a + if it isn't the first term and the coefficient is positive 
            firstoutput = firstoutput+'+ '
        elif coefficients[b] < 0: # Adds a - if the coefficient is negative
            firstoutput = firstoutput+'- '
        if (coefficients[b] != 1 and int(coefficients[b]) != (-1)) or b == len(coefficients)-1: # If the coefficients isn't 1 or -1, or it's the last term, print it in the output
            firstoutput = firstoutput+str(abs(coefficients[b]))
        if b != len(coefficients)-1 and b != len(coefficients)-2: # Adds x^ if the coefficient isn't the last or second last one
            firstoutput = firstoutput+'x^'
            firstoutput = firstoutput+str(len(coefficients)-1-b)+' '
        elif b == len(coefficients)-2: # Only adds x if the coefficient is the second last one
            firstoutput = firstoutput+'x '

print('\nYour input polynomial is: ', firstoutput) # Prints the input polynomial

for m in range(0,tempcoefficients.count(0)): # Removes all terms with coefficient 0 (Descartes Rule of Sign)
    tempcoefficients.remove(0)
    negcoefficients.remove(0)

for a in range(0,len(tempcoefficients)-1): # Uses Descartes Rule of Sign to find possible number of positive roots
    if (tempcoefficients[a]<0 and tempcoefficients[a+1]>0) or (tempcoefficients[a]>0 and tempcoefficients[a+1]<0):
        numposroots = numposroots+1

if x%2 == 1: # Uses Descartes Rule of Sign to find possible number of negative roots
    for a in range(1,int((x-1)/2+1)): # Converts x into -x if the number of coefficients is odd
        negcoefficients[(a*2)-1] = negcoefficients[(a*2)-1]*(-1)
else: # Converts x into -x if the number of coefficients is even (It makes a difference due to having to replace x with -x in Descartes Rule of Sign)
    for a in range(0,math.floor((len(negcoefficients)/2))):
        negcoefficients[a*2] = negcoefficients[a*2]*(-1)

for a in range(0,len(negcoefficients)-1): # Counts number of possible negative roots (Descartes Rule of Sign)
    if (negcoefficients[a] < 0 and negcoefficients[a+1] > 0) or (negcoefficients[a] > 0 and negcoefficients[a+1] < 0):
        numnegroots = numnegroots+1

possrootsn = factors(abs(int(coefficients[0]))) # Finds all factors of the first coefficient
possroots0 = factors(abs(int(coefficients[len(coefficients)-1]))) # Finds all factors of the last coefficient

for a in range(0,len(possrootsn)): # Finds all possible roots using the two lists of factors
    for b in range(0, len(possroots0)):
        if possroots.count(possroots0[b]/possrootsn[a]) == 0:
            possroots.append(possroots0[b]/possrootsn[a])

for a in range(0,x): # Finds all positive roots using the list of possible roots and efficiently checks whether the remaining polynomial is factorable or not (Descartes Rule of Sign + Synthetic Division)
    if not found: # Boolean which is checked to see if the remaining polynomial is factorable or not
        if ((numposroots%2 == 0 and len(totalposroots)%2 == 1) or (numposroots%2 == 1 and len(totalposroots)%2 == 0)): # Uses Descartes Rule of Sign to efficiently tell when it should check whether the polynomial is factorable or not
            for b in range(0,len(possroots)): # Tries to synthetically divide through the entire list of possible roots, and adds the root to a list if there's no remainder
                if synthdiv(coefficients,[1,possroots[b]*(-1)]) != 0:
                    finalpoly.append([1,possroots[b]*(-1)])
                    coefficients=synthdiv(coefficients,[1,(possroots[b])*(-1)])
                    if totalposroots.count(-possroots[b]*(-1)) == 0:
                        totalposroots.append(-possroots[b]*(-1))
        else: # Checks whether the polynomial is factorable or not
            temproot = 0
            for b in range(0,len(possroots)): 
                if synthdiv(coefficients,[1,(possroots[b])*(-1)]) == 0: # If there exist no roots, set the boolean found to True
                    temproot = temproot+1
                else: # Otherwise if it finds a root, add it to the list and continue normally
                    finalpoly.append([1,possroots[b]*(-1)])
                    coefficients = synthdiv(coefficients,[1,(possroots[b])*(-1)])
                    if totalposroots.count(-possroots[b]*(-1)) == 0:
                        totalposroots.append(-possroots[b]*(-1))
            if temproot == len(possroots):
                found = True

found = False # Resets found to False to find negative roots

for a in range(0,x): # Essentially the same as lines 114-134, with the exception that I'm switching the sign on the root to find negative roots
    if not found:
        if ((numnegroots%2 == 0 and len(totalnegroots)%2 == 1) or (numnegroots%2 == 1 and len(totalnegroots)%2 == 0)):
            for b in range(0,len(possroots)):
                if synthdiv(coefficients,[1,possroots[b]]) != 0:
                    finalpoly.append([1,possroots[b]])
                    coefficients = synthdiv(coefficients,[1,possroots[b]])
                    if totalnegroots.count(-possroots[b]) == 0:
                        totalnegroots.append(-possroots[b])
        else:
            temproot = 0
            for b in range(0,len(possroots)):
                if synthdiv(coefficients,[1,possroots[b]]) == 0:
                    temproot = temproot+1
                else:
                    finalpoly.append([1,possroots[b]])
                    coefficients = synthdiv(coefficients,[1,possroots[b]])
                    if totalnegroots.count(-possroots[b]) == 0:
                        totalnegroots.append(-possroots[b])
            if temproot == len(possroots):
                found = True

if coefficients != [1.0]: # If the remaining polynomial is unfactorable and isn't 1, add it to the final list
    finalpoly.append(coefficients)

for a in range(0,len(finalpoly)): # Essentially lines 71-83 again, only it goes through the final list to create a user friendly version
    finaloutput = finaloutput+'( ' # Adds parentheses to indicate each individual term/root/polynomial
    for b in range(0,len(finalpoly[a])):
        if finalpoly[a][b] != 0: # See lines 71-83
            if finalpoly[a][b] > 0 and b != 0:
                finaloutput = finaloutput+'+ '
            elif finalpoly[a][b] < 0:
                finaloutput = finaloutput+'- '
            if int(finalpoly[a][b]) != 1 and int(finalpoly[a][b]) != (-1) and b != len(finalpoly[a])-1:
                if finalpoly[a][b]%1 == 0:
                    finaloutput = finaloutput+str(abs(int(finalpoly[a][b])))
                else:
                    finaloutput = finaloutput+str(abs(finalpoly[a][b]))
            elif b == len(finalpoly[a])-1:
                if finalpoly[a][b]%1 == 0:
                    finaloutput = finaloutput+str(abs(int(finalpoly[a][b])))
                else:
                    finaloutput = finaloutput+str(abs(finalpoly[a][b]))
            if b != len(finalpoly[a])-1 and b != len(finalpoly[a])-2:
                finaloutput = finaloutput+'x^'
                finaloutput = finaloutput+str(len(finalpoly[a])-1-b)+' '
            elif b == len(finalpoly[a])-2:
                finaloutput = finaloutput+'x '
    finaloutput = finaloutput+' )' # Ends the parenthesis placed earlier

print('\n', 'Your polynomial factored boils down to: ', finaloutput)
print('The total number of positive roots you have is: ',len(totalposroots))
print('All positive roots are: ', totalposroots)
print('The total number of negative roots you have is: ',len(totalnegroots))
print('All negative roots are: ', totalnegroots)
