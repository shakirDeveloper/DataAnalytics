# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:18:30 2020

@author: MyFirstLaptop
"""

import unittest
from calc_oop import Calculator_Lambda

#Please comment out line 281 or Main(Calculator_Lambda) before running unit tests

class TestCalculator(unittest.TestCase):
    def test_add_series(self):
        calculator = Calculator_Lambda()
        addList = [5,10,15]
        self.assertEqual(30, calculator.add(addList))
        
    def test_add_lists(self):
        calculator = Calculator_Lambda()
        addList1 = [4,10,3]
        addList2 = [6,10,7]
        self.assertEqual([10,20,10], calculator.addLists(addList1, addList2))
        
    def test_sub_series(self):
        calculator = Calculator_Lambda()
        addList = [1000,-75,-50]
        self.assertEqual(875, calculator.add(addList))
        
    def test_sub_lists(self):
        calculator = Calculator_Lambda()
        addList1 = [-14,100,20]
        addList2 = [16,-50,-7]
        self.assertEqual([2,50,13], calculator.addLists(addList1, addList2))

    def test_mult_series(self):
        calculator = Calculator_Lambda()
        addList = [2,4,8]
        self.assertEqual(64, calculator.multiplication(addList))
        
    def test_multi_lists(self):
        calculator = Calculator_Lambda()
        addList1 = [5,11,3]
        addList2 = [5,2,10]
        self.assertEqual([25,22,30], calculator.multiplicationLists(addList1, addList2))
        
    def test_divid_series(self):
        calculator = Calculator_Lambda()
        addList = [1000,100,2]
        self.assertEqual(5, calculator.division(addList))
        
    def test_divid_list(self):
        calculator = Calculator_Lambda()
        addList1 = [20,10,27]
        addList2 = [2,10,3]
        self.assertEqual([10,1,9], calculator.divisionLists(addList1, addList2))
    
    def test_fact_number(self):
        calculator = Calculator_Lambda()
        addList = 5
        self.assertEqual(120, calculator.factorial(addList))
        
    def test_fact_list(self):
        calculator = Calculator_Lambda()
        addList = [5,4,3]       
        self.assertEqual([120,24,6], calculator.factorialList(addList))
    
    def test_cube_list(self):
        calculator = Calculator_Lambda()
        addList = [10,6,7]       
        self.assertEqual([1000,216,343], calculator.cubeList(addList))
    
    def test_square_list(self):
        calculator = Calculator_Lambda()
        addList = [4,11,1]       
        self.assertEqual([16,121,1], calculator.squareList(addList))
    
    def test_halfOfNumber_list(self):
        calculator = Calculator_Lambda()
        addList = [4,10,81]       
        self.assertEqual([2,5,40.5], calculator.halfOfNumberList(addList))
        
    def test_log_list(self):
        calculator = Calculator_Lambda()
        addList = [1,3,10]       
        self.assertEqual([0,1.10,2.30], calculator.logOfNumberList(addList))
        
    def test_exponential_list(self):
        calculator = Calculator_Lambda()
        addList = [2,4,6]       
        self.assertEqual([7.39,54.6,403.43], calculator.exponantialOfNumberList(addList))
    
    def test_fitler_even_number_list(self):
        calculator = Calculator_Lambda()
        addList = [2,4,6,7,9,13]       
        self.assertEqual([7,9,13], calculator.filterEvenNumberList(addList))
        
if __name__ == '__main__':
    unittest.main()