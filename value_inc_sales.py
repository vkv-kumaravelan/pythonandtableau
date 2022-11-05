# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:50:34 2022

@author: vkvku
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')  <---- format of read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the datat
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathametical operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction column calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchase
#variable = dataframe['column_name']
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column in dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation = sales - cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost) / cost
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Rounding Marking
roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#combining data fields
my_name = 'vkv' + 'kumaravelan'

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#my_date = data['Day']+'-'

#checking columns data type
print(data['Day'].dtype)

#change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] #views the rows with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.head(5) #brings in first 5 rows
data.iloc[:,2] #brings in all rows on the 2nd column
data.iloc[4,2] #brings in 4th row 2nd column

#using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)
Split_col =  data['ClientKeywords'].str.split(',' , expand = True)

#creating a new columns for the split columns in keywords
data['ClientAge'] = Split_col[0]
data['ClientType'] = Split_col[1]
data['LengthofContract'] = Split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns
#df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Year', axis = 1)
data = data.drop('Month', axis = 1)
data = data.drop('Day', axis = 1)

#multiple dropping columns
#df = df.drop(['columnname1', 'columnname2'], axis = 1)

#Export into CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)
































































































































