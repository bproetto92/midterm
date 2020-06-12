#
# QUESTION 1
#


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print("------------------")
print("PROCESSING PRODUCTS INVENTORY...")
print("------------------")

#
# PART A
#


print("HELLO")

 # todo: write some Python code here to answer the question!


#
# PART B
#
name = []

for id in products:
  if id["id"] == 19:
      name.append(id["name"])

print(name[0]) # todo: write some Python code here to answer the question!

total_price = 0
for id in products:
  total_price = total_price + id["price"]

print(total_price)