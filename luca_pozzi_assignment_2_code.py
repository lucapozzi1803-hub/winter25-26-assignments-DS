
# Install NumPy and check the version

# %pip install numpy
import numpy as np
print(np.__version__)

### Part 1: NumPy Array Manipulation (The Core Data) ###________________________

### 1. Create Product Data 

np.random.seed(0)  # seed for reproducibility

product_ids = np.arange(1000,1010) # 1-dimensional array
product_ids

# Creation of columns before using the stack command

stock = np.random.randint(10, 120, size = 10, dtype = 'int64')
avg_w_sales = np.random.uniform(3.2, 25.0, size = 10)
avg_w_sales = np.round(avg_w_sales, 2) # rounding the floats to 2 decimal places
unit_cost = np.random.uniform(5.00, 50.50, size = 10)
unit_cost = np.round(unit_cost, 2) # rounding the floats to 2 decimal places
print(stock, avg_w_sales, unit_cost)

# Stacking the columns into a 10,3 array

inventory_data = np.column_stack((stock, avg_w_sales, unit_cost))
inventory_data




# I wasn't sure about the correct method for creating a 10, 3 array with different data types so I created 3 seperate columns and stack them into a single array.



###  2. Basic calculations and attributes

print("Inventory shape: ", inventory_data.shape) # Shape of the inventory data array
print("Inventory data type: ", inventory_data.dtype) # Data type of the inventory data array

total_value = stock * unit_cost # Total value of the current stock for all products
print(total_value)



# 3. Slicing, Indexing, and Statistics:

product_3_7 = inventory_data[3:8]# Extract the data from product 3 to 7 (inclusive)
print("Products from 3 to 7: ", product_3_7)

avg_w_sales_mean = np.mean(avg_w_sales) # Extract the average of the Average Weekly Sales across all 10 products
avg_w_sales_mean = np.round(avg_w_sales_mean, 2)
print("Average weekly sales (mean): ", avg_w_sales_mean)

unit_cost_1st_product = inventory_data[0,2] # Unit cost of the 1st product
print("Unit cost of the first product: ", unit_cost_1st_product)




### Part 2: Advanced NumPy Analysis (Re-stocking Logic) ###______________________

### 1. Boolean Masking (The "Low-Stock" Check):

weeks_of_stock = stock / avg_w_sales # Calculate the number of weeks the current stock will last based on average sales.
weeks_of_stock = np.round(weeks_of_stock, 2)
print("Remaining weeks of stock: ", weeks_of_stock)

low_stock = (weeks_of_stock < 4) # Create a boolean mask that is True for any product where the Weeks of Stock is less than 4 (i.e., less than a month's supply).
low_stock_products = inventory_data[low_stock] # Extract and print the entire rows from inventory_data for the products that are low in stock.
print("Low stock products: ", low_stock_products)



### 2. Reshaping and Concatenation (Updating Data):

reorder_quantity = np.array((4 * avg_w_sales) - stock) # Create a new 1-dimensional NumPy array named reorder_quantity where each value is calculated as: (4 * Average Weekly Sales) - Current Stock Level (i.e., enough to bring stock up to a 4-week supply).
reorder_quantity = np.abs(reorder_quantity) # Return absolute values
print(reorder_quantity)

reorder_quantity_2D = reorder_quantity.reshape(10, 1) # Reshape the reorder_quantity array to a (10, 1) 2D array.
print(reorder_quantity_2D)

new_inventory_data = np.concatenate ((inventory_data,reorder_quantity_2D), axis=1)
print("New reordered inventory: ", new_inventory_data) # Combine the original inventory_data array with the new reorder_quantity array along the appropriate axis (resulting in a (10, 4) array).



### Part 3: Introduction to Pandas (Viewing the Results) ###_________________

# %pip install pandas
import pandas as pd

### 1. Create a DataFrame:

df_inventory = pd.DataFrame(new_inventory_data, columns = ['Stock', 'Sales', 'Cost', 'Reorder Qty']) # Create a Pandas DataFrame and assign the appropriate columns name



### 2. Basic Selection:
 
print(df_inventory[['Stock', "Reorder Qty"]]) # Print only Stock and Reorder Qty columns

print(df_inventory.head(5)) # Print the first 5 rows of the DataFrame.


