# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:02:57 2020

@author: MyFirstLaptop
"""
import numpy as np
import csv
import pandas as pd
import codecs
import matplotlib.pyplot as plt
from numpy import int64

path1 = 'C:\\CA4\\Census2011.csv'
path2 = 'C:\\CA4\\Census2016.csv'

title_data = []
columns_name = ''
index_columns = []

def readExcelSheet(path):
    csv_data = []
    count =0
    with codecs.open(path, 'rU', 'utf-16') as csv_file:        
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            if len(row) != 0 and count > 1 :
                csv_data.append(row)                            
            count = count + 1   
    #return np.array(csv_data)[1:,1:]
    return np.array(csv_data)

def get_calculation_columns(matrix):
    return matrix[1:,1:]

def get_title_columns_name(matrix): 
    global columns_name
    global index_columns
    columns_name = matrix[0,1:]
    index_columns = matrix[1:,0]


def calculate_censuses_ratio(matrix1, matrix2):
    get_title_columns_name(matrix2)
    global columns_name
    global index_columns
    
    female_data_2016 = get_calculation_columns(matrix1)[:,1]
    female_data_2011 = get_calculation_columns(matrix2)[:,1]
    
    male_data_2016 = get_calculation_columns(matrix1)[:,0]
    male_data_2011 = get_calculation_columns(matrix2)[:,0]
    
    percentage_female =((np.array( female_data_2016, dtype=int) - np.array(female_data_2011, dtype=int))/np.array( female_data_2016, dtype=int))*100
    #print(percentage_female)
    #print(male_data_2011)
    df_female  = pd.DataFrame(percentage_female, index=index_columns, columns =['female population increase(%)'])
    
    percentage_male =(np.array( male_data_2016, dtype=int) - np.array(male_data_2011, dtype=int)/np.array( male_data_2016, dtype=int))*100
    df_male  = pd.DataFrame(percentage_male, index=index_columns, columns =['male population increase(%)'])
    #save_csv(c)
    print('Increase/Decrease in Percentage of female population during census 2011 and 2016 group by age')
    print(np.array( df_female, dtype=complex ) )
    print('Increase/Decrease in Percentage of male population during census 2011 and 2016 group by age')
    print(np.array( df_male, dtype=complex ))

def total_female_graph_by_year(matrix1, matrix2):
    get_title_columns_name(matrix2)
    global columns_name
    global index_columns
    
    female_data_2016 = get_calculation_columns(matrix1)[:-1,1]
    female_data_2011 = get_calculation_columns(matrix2)[:-1,1]
    
    male_data_2016 = get_calculation_columns(matrix1)[:-1,0]
    male_data_2011 = get_calculation_columns(matrix2)[:-1,0]    
    
    male_data_2011=male_data_2011.astype('int32')
    male_data_2016=male_data_2016.astype('int32') 
    female_data_2011=female_data_2011.astype('int32') 
    female_data_2016=female_data_2016.astype('int32')     
    
    print(np.arange(68).reshape(34, 2))
    
    plt.close('all')
    #Plot female graph of both censuses
    df = pd.DataFrame(np.column_stack(([female_data_2011,female_data_2016] )), index=index_columns[:-1], columns= ['2011','2016'])
    df=df.astype(int64)
    print('female population of 2011 and 2016 by age group')
    print(df)
    

    plt.figure()
    df.plot()
    plt.title('Number of female by age group ')
    plt.xlabel('age group')
    plt.ylabel('Population')
    plt.legend(loc='best')
    
    #Plot male graph of both censuses
    df = pd.DataFrame(np.column_stack(([male_data_2011,male_data_2016] )), index=index_columns[:-1], columns= ['2011','2016'])  
    df=df.astype(int64)
    print('male population of 2011 and 2016 by age group')
    print(df)
    
    plt.figure()
    df.plot()
    plt.title('Number of male by age group ')
    plt.xlabel('age group')
    plt.ylabel('Population')
    plt.legend(loc='best')
    
def calculate_censuses_difference(matrix1, matrix2):
    get_title_columns_name(matrix2)
    global columns_name
    global index_columns    
    diff =np.array( get_calculation_columns(matrix2), dtype=int) - np.array(get_calculation_columns(matrix1), dtype=int)
    df  = pd.DataFrame(diff, index=index_columns, columns =columns_name)    
    print('Difference of male and female population of census 2011 and 2016 group by age')  
    print(df)
    
def calc_mean_female_population(matrix1, matrix2):
    female_data_2016 = get_calculation_columns(matrix1)[:-1,1]
    female_data_2011 = get_calculation_columns(matrix2)[:-1,1]
    
    female_data_2011=female_data_2011.astype('int32') 
    female_data_2016=female_data_2016.astype('int32') 
    df = pd.DataFrame(np.column_stack(([female_data_2011,female_data_2016] )), index=index_columns[:-1], columns= ['2011','2016'])
    
    print('mean of female population by year')
    print(df.mean().round(2))
    
def calc_mean_male_population(matrix1, matrix2):
    male_data_2016 = get_calculation_columns(matrix1)[:-1,0]
    male_data_2011 = get_calculation_columns(matrix2)[:-1,0]
   
    male_data_2011=male_data_2011.astype('int32') 
    male_data_2016=male_data_2016.astype('int32') 
    df = pd.DataFrame(np.column_stack(([male_data_2011,male_data_2016] )), index=index_columns[:-1], columns= ['2011','2016'])
        
    print('mean of male population by year')
    print(df.mean().round(2))

def description_2011_census(matrix):
    df = pd.DataFrame(matrix[1:,:-1], index=index_columns, columns= ['Age','Male','Female'])
    print(df.describe())

def description_2016_census(matrix):   
    df = pd.DataFrame(matrix[1:,:-1], index=index_columns, columns= ['Age','Male','Female'])
    print(df.describe())
def main():
    a = readExcelSheet(path1)
    b = readExcelSheet(path2)
    calculate_censuses_difference(b,a)
    calculate_censuses_ratio(b,a)
    total_female_graph_by_year(b,a)
    calc_mean_female_population(b,a)
    calc_mean_male_population(b,a)
    description_2011_census(a)
    description_2016_census(b)

main()
