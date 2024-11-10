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

