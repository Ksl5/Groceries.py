# groceries.py
#from pprint import pprint

import csv
# todo: assemble a new products variable by reading from CSV file
products = []
csv_filepath = "products.csv" # a relative filepath
with open(csv_filepath, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        # print(type(row)) #> <class 'collections.OrderedDict'>
        #print(type(row), row["id"], row["name"], row["price"])
        #products.append(row) #> gives us price values as string
        row["price"] = float(row["price"]) # change the price from string to float
        products.append(row)



#products = [
# {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
# {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
# {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
# {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
# {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
# {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
# {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
# {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
# {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
# {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
# {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
# {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
# {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
# {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
# {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
# {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
# {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
# {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
# {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
# {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
#] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#
#Products (Part 1)
#





print(type(products)) #> list

# COUNT THE PRODUCTS
products_count = 20

print("------------")
print("THERE ARE " + str(products_count) + " PRODUCTS:")
print("------------")

#print("NUMBER OF PRODUCTS:", len(products)) #>leaving prof's notes

# LOOP THROUGH THE PRODUCTS AND PRINT EACH ONE

def sort_by_name(any_product):
        return any_product["name"]

sorted_products = sorted(products, key=sort_by_name)

for x in sorted_products:
    #print("-----")
    #print(type(x))
    #print(x)
    #print("name")
    #print(x["name"])
    
    #price_usd = x["price"] #>"4.99"]
    price_usd = "${0:.2f}".format(x["price"])   
    print("+ " + x["name"] + " (" + str(price_usd) + ")")

    

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#
#Departments (Part 2)
#

# COUNT THE DEPARTMENTS

departments = []
for x in products:
    #print (x["department"])
    departments.append(x["department"])
    #if x["department"] not in departments:
    #    departments.append(x["department"])

unique_departments = list(set(departments))

department_count = len(unique_departments)
   
print("------------")
print("THERE ARE " + str(department_count) + " DEPARTMENTS:")
print("------------")

#filter()

unique_departments.sort()
for d in unique_departments:
    matching_products = [x for x in products if x["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"

    print("+" + d.title()+ " (" + str(matching_products_count) + " " + label +")")


