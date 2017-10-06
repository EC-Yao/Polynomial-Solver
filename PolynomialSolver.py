# This code will take in a series of inputs from the user, representing a desired polynomial. It will
# then attempt to factor the polynomial using a series of mathematical properties and return the 
# factored form to the user.
#   - Eddy Yao

# Instances and imports necessary libraries
import math
import sys

x = 0 
y = 0
coefficients = []
tempList = []
possibleRootsN = []
possibleRootsZero = []
possibleRoots = []
tempCoefficients = []
negCoefficients = []
numberOfPositiveRoots = 0
numberOfNegativeRoots = 0
found = False
tempRoot = 0
totalPositiveRoots = []
totalNegativeRoots = []
finalPolynomial = []
firstOutput = ''
finalOutput = ''

# Synthetically divide a polynomial by another, as represented by integer lists.
def syntheticDivision(dividend, divisor):
    divis = list(dividend)
    divid = divisor[0]
    for a in range(len(dividend)-(len(divisor)-1)):
        divis[a] /= divid 
        coef = divis[a]
        if coef != 0:
            for b in range(1, len(divisor)):
                divis[a + b] += -divisor[b] * coef
    separator = -(len(divisor)-1)
    if divis[separator:] == [0.0]:
        return divis[:separator]
    else:
        return 0

# Returns all factors of an integer input
def factors(x):
    global tempList
    tempList = []
    for a in range(1,int(math.floor(math.sqrt(x))+1)):
        if x%a == 0:
            tempList.append(a)
            tempList.append(int(x/a))
    if math.sqrt(x)%1 == 0:
        tempList.remove(math.sqrt(x))
    tempList.sort()
    return tempList

print("""
This is a polynomial factoring code
Eddy Yao, January 5, 2016
We don't accept fraction coefficients, sorry!
""")

# Harvests the inputs from the user
x = int(input('Degree of polynomial?'))
if x < 0 or x%1 != 0:
    print('Nice try')
    sys.exit()
x += 1
y = int(input('What is the coefficient of the highest power? (Include powers with 0 coefficient)'))
coefficients.append(y)
negCoefficients.append(y)
tempCoefficients.append(y)

for a in range(0,x-1):
    y = int(input('What is the coefficient of the next highest power? (Include powers with 0 coefficient)'))
    coefficients.append(y)
    negCoefficients.append(y)
    tempCoefficients.append(y)

# Builds a string based on the input polynomial and returns it to the user
for b in range(0,len(coefficients)):
    if coefficients[b] != 0:
        if coefficients[b] > 0 and b != 0:
            firstOutput = firstOutput+'+ '
        elif coefficients[b] < 0:
            firstOutput = firstOutput+'- '
        if (coefficients[b] != 1 and int(coefficients[b]) != (-1)) or b == len(coefficients)-1:
            firstOutput = firstOutput+str(abs(coefficients[b]))
        if b != len(coefficients)-1 and b != len(coefficients)-2:
            firstOutput = firstOutput+'x^'
            firstOutput = firstOutput+str(len(coefficients)-1-b)+' '
        elif b == len(coefficients)-2:
            firstOutput = firstOutput+'x '

print('\nYour input polynomial is: ', firstOutput)

# Removes all terms with coefficient 0 in order to apply Descartes Rule of Sign
for m in range(0,tempCoefficients.count(0)):
    tempCoefficients.remove(0)
    negCoefficients.remove(0)

# Applies Descartes Rule of Sign to find the potential number of positive and negative roots
for a in range(0,len(tempCoefficients)-1):
    if (tempCoefficients[a]<0 and tempCoefficients[a+1]>0) or (tempCoefficients[a]>0 and tempCoefficients[a+1]<0):
        numberOfPositiveRoots = numberOfPositiveRoots+1

if x%2 == 1:
    for a in range(1,int((x-1)/2+1)):
        negCoefficients[(a*2)-1] = negCoefficients[(a*2)-1]*(-1)
else:
    for a in range(0,math.floor((len(negCoefficients)/2))):
        negCoefficients[a*2] = negCoefficients[a*2]*(-1)

for a in range(0,len(negCoefficients)-1):
    if (negCoefficients[a] < 0 and negCoefficients[a+1] > 0) or (negCoefficients[a] > 0 and negCoefficients[a+1] < 0):
        numberOfNegativeRoots = numberOfNegativeRoots+1

# Finds all possible roots of the input polynomial
possibleRootsN = factors(abs(int(coefficients[0])))
possibleRootsZero = factors(abs(int(coefficients[len(coefficients)-1])))

for a in range(0,len(possibleRootsN)):
    for b in range(0, len(possibleRootsZero)):
        if possibleRoots.count(possibleRootsZero[b]/possibleRootsN[a]) == 0:
            possibleRoots.append(possibleRootsZero[b]/possibleRootsN[a])
            
# Finds all positive roots using the list of possible roots and prior calculations to save time
for a in range(0,x):
    if not found:
        if ((numberOfPositiveRoots%2 == 0 and len(totalPositiveRoots)%2 == 1) or (numberOfPositiveRoots%2 == 1 and len(totalPositiveRoots)%2 == 0)):
            for b in range(0,len(possibleRoots)):
                if syntheticDivision(coefficients,[1,possibleRoots[b]*(-1)]) != 0:
                    finalPolynomial.append([1,possibleRoots[b]*(-1)])
                    coefficients=syntheticDivision(coefficients,[1,(possibleRoots[b])*(-1)])
                    if totalPositiveRoots.count(-possibleRoots[b]*(-1)) == 0:
                        totalPositiveRoots.append(-possibleRoots[b]*(-1))
        else:
            tempRoot = 0
            for b in range(0,len(possibleRoots)): 
                if syntheticDivision(coefficients,[1,(possibleRoots[b])*(-1)]) == 0:
                    tempRoot = tempRoot+1
                else:
                    finalPolynomial.append([1,possibleRoots[b]*(-1)])
                    coefficients = syntheticDivision(coefficients,[1,(possibleRoots[b])*(-1)])
                    if totalPositiveRoots.count(-possibleRoots[b]*(-1)) == 0:
                        totalPositiveRoots.append(-possibleRoots[b]*(-1))
            if tempRoot == len(possibleRoots):
                found = True

found = False

# Does the same as above only for negative roots
for a in range(0,x):
    if not found:
        if ((numberOfNegativeRoots%2 == 0 and len(totalNegativeRoots)%2 == 1) or (numberOfNegativeRoots%2 == 1 and len(totalNegativeRoots)%2 == 0)):
            for b in range(0,len(possibleRoots)):
                if syntheticDivision(coefficients,[1,possibleRoots[b]]) != 0:
                    finalPolynomial.append([1,possibleRoots[b]])
                    coefficients = syntheticDivision(coefficients,[1,possibleRoots[b]])
                    if totalNegativeRoots.count(-possibleRoots[b]) == 0:
                        totalNegativeRoots.append(-possibleRoots[b])
        else:
            tempRoot = 0
            for b in range(0,len(possibleRoots)):
                if syntheticDivision(coefficients,[1,possibleRoots[b]]) == 0:
                    tempRoot = tempRoot+1
                else:
                    finalPolynomial.append([1,possibleRoots[b]])
                    coefficients = syntheticDivision(coefficients,[1,possibleRoots[b]])
                    if totalNegativeRoots.count(-possibleRoots[b]) == 0:
                        totalNegativeRoots.append(-possibleRoots[b])
            if tempRoot == len(possibleRoots):
                found = True

# Includes the rest of the polynomial in case it isn't perfectly factorable
if coefficients != [1.0]:
    finalPolynomial.append(coefficients)

# Builds a string based on the desired output from the calculations done
for a in range(0,len(finalPolynomial)):
    finalOutput = finalOutput+'( '
    for b in range(0,len(finalPolynomial[a])):
        if finalPolynomial[a][b] != 0:
            if finalPolynomial[a][b] > 0 and b != 0:
                finalOutput = finalOutput+'+ '
            elif finalPolynomial[a][b] < 0:
                finalOutput = finalOutput+'- '
            if int(finalPolynomial[a][b]) != 1 and int(finalPolynomial[a][b]) != (-1) and b != len(finalPolynomial[a])-1:
                if finalPolynomial[a][b]%1 == 0:
                    finalOutput = finalOutput+str(abs(int(finalPolynomial[a][b])))
                else:
                    finalOutput = finalOutput+str(abs(finalPolynomial[a][b]))
            elif b == len(finalPolynomial[a])-1:
                if finalPolynomial[a][b]%1 == 0:
                    finalOutput = finalOutput+str(abs(int(finalPolynomial[a][b])))
                else:
                    finalOutput = finalOutput+str(abs(finalPolynomial[a][b]))
            if b != len(finalPolynomial[a])-1 and b != len(finalPolynomial[a])-2:
                finalOutput = finalOutput+'x^'
                finalOutput = finalOutput+str(len(finalPolynomial[a])-1-b)+' '
            elif b == len(finalPolynomial[a])-2:
                finalOutput = finalOutput+'x '
    finalOutput = finalOutput+' )'
    
# Prints out the results from the program
print('\n', 'Your polynomial factored boils down to: ', finalOutput)
print('The total number of positive roots you have is: ',len(totalPositiveRoots))
print('All positive roots are: ', totalPositiveRoots)
print('The total number of negative roots you have is: ',len(totalNegativeRoots))
print('All negative roots are: ', totalNegativeRoots)


