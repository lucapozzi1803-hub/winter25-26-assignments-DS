
# Install NumPy and check the version

import pandas as pd

# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)


# Assignment 3: Global Sales Data Analyst

## Part 1: Reading and inspecting data ##____________________________________

# Read the data from the provided .csv file into a pandas DataFrame

df = pd.read_csv("global_sales.csv")

# Print the first 5 rows and the data types of all columns using appropiate DataFrame methods

df.info()
df.head(5)




### Part 2: Data Cleaning and Indexing ### _____________________

## 1. Handling Missing Values and Casting:
# Fill Missing Values: Replace the missing values (NaN) in the Units_Sold column with the mean value of the entire column.

df.isna() # Check for NaN



mean_units_sold = df['Units_Sold'].mean() # Create the column mean
mean_units_sold = round(mean_units_sold)
df['Units_Sold'] = df['Units_Sold'].fillna(mean_units_sold) # fill NaN values in Unit Sold with the mean
df


# How to round those means? 


# Data Type Casting: Convert the Sales column to a numeric data type (float). 
# Handle any remaining non-numeric values during conversion (e.g., by coercing them to NaN and then filling them with 0).

df.dtypes


df['Sales'] = df['Sales'].fillna(0) # filling NaN with '0'


# Casting Dates: Convert the Date column to a proper datetime object.

df['Date'].dtypes
df['Date'] = pd.to_datetime(df['Date'])
df.dtypes


## 2. Indexing and Setting:
# Use the OrderID column to set a new index for the DataFrame.

df.set_index('OrderID')


# Reset the index, and then set the Date column as the index. This makes the DataFrame suitable for time series analysis.

df = df.reset_index()
df = df.set_index('Date')
df.index # Check the index in place



### Part 3: Filtering, Modifying, and Sorting ### _______________________

## 1. Filtering Data:

# Create a new DataFrame named high_value_sales that contains only the sales records where the Sales amount is greater than $500 AND the Region is 'Europe'. 
# Print the head of this new DataFrame.

high_value_sales = df[(df['Sales'] > 500) & (df['Region'] == 'Europe')]
high_value_sales.head()


## 2. Updating and Adding Columns:

# Update a Row: Select a specific row (e.g., the 5th row of the original DataFrame) and modify its Units_Sold value to 99.

df.loc[df.index[4], 'Units_Sold'] = 99
df


#  Add a Column: Add a new column named Profit calculated as: Profit = Sales * 0.20.

df['Profit'] = (df['Sales'] * 0.20).round(2)
df


## 3. Sorting Data:

# Sort the DataFrame first by Region (ascending) and then by Sales (descending). Print the first few rows of the sorted DataFrame.

sorted_region = df.sort_values(by='Region', ascending = True)
sorted_region.head(5)


sorted_sales = df.sort_values(by='Sales', ascending = False)
sorted_sales.head(5)


### Part 4: Grouping and Aggregation (Analysis) ### _____________________

## 1. Regional Performance:

# Group the data by Region and calculate the total sum of Sales and the average Units_Sold for each region. Print the result.

region_grp = df.groupby(['Region'])

region_grp['Sales'].sum() # total sum of Sales per region

region_grp['Units_Sold'].mean() # average Units_Sold per region


## 2. Product Deep Dive:

# Group the data by Product and find the maximum Profit achieved for each product type. Print the result.

max_profit_grp = df.groupby('Product')['Profit'].max()
max_profit_grp


## 3. Time Series Analysis (Bonus/Challenge):

# Since the Date column is the index, use a time-based resampling method (e.g., .resample('M')) to calculate the monthly total sales. Print the result.

monthly_tot_sales = df['Sales'].resample('ME').sum()
monthly_tot_sales


