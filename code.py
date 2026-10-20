# step : 1

# Name : Retail Sales Analysis

# Using : Python and Pandas

#------------------------------------------------------------------------------>

# importing Libraries

import pandas as pd    

import matplotlib.pyplot as plt 


#------------------------------------------------------------------------------>

# dataSet Table

data = {

    "Product" : [ "Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse", "Keyboard", "Laptop", ], 

    "City" : [ "Vizag", "Hyderabad", "Chennai", "Vizag", "Chennai", "Hyderabad", "Vizag", "Chennai" ],

    "Sales" : [ 50000, 500, 1500, 45000, 12000, 800, 2000, 55000 ],

    "Quantity" : [2, 10, 5, 2, 3, 16, 5, 2]

}

df = pd.DataFrame(data)

#print(df)


#------------------------------------------------------------------------------>

# step : 2 > inspect the data : (4)


#print(df.head())    # head() displays the 1st five Rows (1)


#print(df.shape)    # shape() gives the number of Rows & Cols (2)


#print(df.info())   # info() shows column data types & non-missing counts (3)


#print(df.isnull().sum())    # isnull().sum() counts missing values in each column (4)



#note : for this datset, you should find 8 rows, 4 columns, and no missing values


#------------------------------------------------------------------------------>

# step : 3 > calculate Total revenue : 
# lets answer the 1st business Question 

'''

total_revenue = df["Sales"].sum()    # <- logic

print("Total revenue :", total_revenue)


'''

#op : Total revenue : 166800 

#------------------------------------------------------------------------------>

# step : 4 > Find the best-performing product :
# lets Group the sales records by product.


'''

product_sales = (

    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)    # <- logic

)

print(product_sales)


'''

# top product : Laptop - ₹1,50,000

#------------------------------------------------------------------------------>

# step : 5 > Find the best-performing city :


'''

city_sales = (

    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)    # <- logic

)

print(city_sales)


'''

# top city : Vizag - ₹97,000


#------------------------------------------------------------------------------>

# step : 6 > Create a Chart :
# A chart makes your findings easier to communicate to a manager.



city_sales = (

    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)    # <- logic

)


city_sales.plot(kind="bar")

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()






























































