# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:58:25 2020

@author: MyFirstLaptop
"""
import functools
import math 

class Calculator_Lambda(object):
    def add(self,figuresToAdd):
        result = functools.reduce(lambda x, y: x+y, figuresToAdd)
        return result
    
    def addLists(self,list1ToAdd, list2ToAdd):
        result = list(map(lambda x, y: x+y, list1ToAdd, list2ToAdd))
        return result
        
    def multiplication(self,figuresToMultiply):
        result = functools.reduce(lambda x, y: x*y, figuresToMultiply)
        return result
    
    def multiplicationLists(self,list1ToMultiply, list2ToMultiply):
        result = list(map(lambda x, y: x*y, list1ToMultiply, list2ToMultiply))
        return result
        
    def cubeList(self,listToCube):
        result = list(map(lambda x: x*x*x, listToCube))
        return result
        
    def squareList(self,listToSquare):
        result = list(map(lambda x: x*x, listToSquare))
        return result
        
    def halfOfNumberList(self,figuresToHalf):
        result = list(map(lambda x: x/2, figuresToHalf))
        return result
    
    def logOfNumberList(self,figuresToLog):
        result = list(map(lambda x: round(math.log(x),2), figuresToLog))
        return result
    
    def exponantialOfNumberList(self,figuresToExponantial):
        result = list(map(lambda x: round(math.exp(x),2), figuresToExponantial))
        return result
    
    def division(self,figuresToDivision):
        result = functools.reduce(lambda x, y: round(x/y,2), figuresToDivision)
        return result
    
    def divisionLists(self,list1ToDivision,list2ToDivision):
        result = list(map(lambda x, y: round(x/y,2), list1ToDivision, list2ToDivision))
        return result
    
    def factorial(self,n):
        if n == 0:
            return 1
        else:
            return functools.reduce(lambda x,y: x*y, range(1,n+1))
    def factorialList(self,figureList):        
        return [ functools.reduce(lambda x,y: x*y, range(1,i+1)) for i in figureList]

    def filterEvenNumberList(self,numberList):
        result = list(filter(lambda x: x % 2, numberList))
        return result
    
def Main(Calculator_Lambda):
    calculator = Calculator_Lambda()
    while True:
        print('1 - for addition/Substraction of list')
        print('2 - for Multiply of list')
        print('3 - for Division of list')
        print('4 - for Factorial of list')
        print('5 - for Cube of list')
        print('6 - for Square of list')
        print('7 - for Divided by 2 of list')
        print('8 - for log 2/ln of list')
        print('9 - for Exponential of list')
        print('10 - for Filter out even number from List')
        inputOperation = int(input('Please enter a above choice or press other key to exit: '))
        if (inputOperation == 1):            
            while 1:
                addSubInput = int(input('Please enter 0 for add/sub figures or 1 for add/sub two lists : '))
                if (addSubInput == 0) :
                    lst = []  
                    n = int(input("Enter total number of elements you want to perform operation : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number with sign i.e. + or - : ".format(i+1)))
                        lst.append(ele)
                    print(calculator.add(lst))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
                elif (addSubInput == 1) :
                    lst1 = []
                    lst2 = []  
                    n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 1st list with sign i.e. + or - : ".format(i+1)))
                        lst1.append(ele)                    
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 2nd list with sign i.e. + or - : ".format(i+1)))
                        lst2.append(ele)
                    print(calculator.addLists(lst1,lst2))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
                else:
                    break
        elif (inputOperation == 2) :
            while 1:
                multiplyInput = int(input('Please enter 0 for multiple figures or 1 for multiply two lists : '))
                if (multiplyInput == 0) :
                    lst = []  
                    n = int(input("Enter total number of elements you want to perform operation : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number : ".format(i+1)))
                        lst.append(ele)
                    print(calculator.multiplication(lst))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
                elif (multiplyInput == 1) :
                    lst1 = []
                    lst2 = []  
                    n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                        lst1.append(ele)                    
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 2nd list : ".format(i+1)))
                        lst2.append(ele)
                    print(calculator.multiplicationLists(lst1,lst2))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
        elif (inputOperation == 3) :
            while 1:
                divisionInput = int(input('Please enter 0 for divide figures or 1 for divide two lists : '))
                if (divisionInput == 0) :
                    lst = []  
                    n = int(input("Enter total number of elements you want to perform operation : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number : ".format(i+1)))
                        lst.append(ele)
                    print(calculator.division(lst))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
                elif (divisionInput == 1) :
                    lst1 = []
                    lst2 = []  
                    n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                        lst1.append(ele)                    
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 2nd list : ".format(i+1)))
                        lst2.append(ele)
                    print(calculator.divisionLists(lst1,lst2))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
        elif (inputOperation == 4) :
            while 1:
                factorialInput = int(input('Please enter 0 for factorial a figure or 1 for list factorial : '))
                if (factorialInput == 0) :
                    lst = []  
                    n = int(input("Enter number you want to perform operation : ")) 
                    print(calculator.factorial(n))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
                elif (factorialInput == 1) :
                    lst1 = []                    
                    n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                    for i in range(0, n): 
                        ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                        lst1.append(ele)
                    print(calculator.factorialList(lst1))
                    continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                    if(continueCalc.lower() == 'y' ):
                        continue
                    else:
                        break
        elif (inputOperation == 5) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.cubeList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        elif (inputOperation == 6) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.squareList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        elif (inputOperation == 7) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.halfOfNumberList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        elif (inputOperation == 8) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.logOfNumberList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        elif (inputOperation == 9) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.exponantialOfNumberList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        elif (inputOperation == 10) :
            while 1:                
                lst1 = []                    
                n = int(input(" Enter total number of elements of lists (Size of list) (Size of list) : ")) 
                for i in range(0, n): 
                    ele = int(input("Enter {0} number of 1st list : ".format(i+1)))
                    lst1.append(ele)
                print(calculator.filterEvenNumberList(lst1))
                continueCalc = input('Do you want to continue enter Y for yes and N for no : ')
                if(continueCalc.lower() == 'y' ):
                    continue
                else:
                    break
        else:
            break
#Please comment out line 281 or following line before running unit tests
Main(Calculator_Lambda)