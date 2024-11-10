import pandas as pd
from FoodItemClass import FoodItem
from orderClass import Order
def newOrderIndexes(df):
  firstRow = True
  listIndexes = []
  orderList = []
  for index, row in df.iterrows():
    if (firstRow):
      prev = row[0]
      date = row[1]
      listIndexes += [index]
      a = Order(date)
      orderList += [a]
      firstRow = False
    else:
      current = row[0]
      if (prev != current):
        prev = current
        date = row[1]
        listIndexes += [index]
        a = Order(date)
        orderList += [a]
  return orderList, listIndexes

# Read in the file, order number can be added after being sorted
# if reading in 
def getFoodIndexes(combined_df):
    indexes = []
    indexes.append(0)

    for index, row in combined_df.iterrows():
        # case for mac and cheese
        # if either the next row has noodles or isn't mac and cheese append that index
        if (index == (len(combined_df)) ):
            break
        if row[4] == "Mac and Cheese":
            if (row[4] != combined_df.iloc[index + 1][4]) or (combined_df.iloc[index+1][3] == "Noods"):
                indexes.append(index + 1)
        if row[4] == "Grilled Cheese Sandwich":
            if (row[4] != combined_df.iloc[index+1][4]) or (combined_df.iloc[index+1][3] == "Choose Your Meats"):
                indexes.append(index + 1)
        if row[4] == "Sides/Desserts":
            indexes.append(index + 1)
        if row[4] == "Drinks":
            indexes.append(index+1)
        if row[4] == "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":
            indexes.append(index+1)
        print(index)


    indexes += (len.df())
    return indexes


# Various statistical tests
combined_df = pd.read_csv("combined_sheets_with_june.csv")
# orderslist = []
# for index, row in combined_df.iterrows():
#     ordernumber = row[0]
#     currentOrder_df = combined_df.iloc(index)
    
#     addOrder(orderslist, currentOrder_df)
print(combined_df.dtypes)
myindexes = getFoodIndexes(combined_df)
print (myindexes)



