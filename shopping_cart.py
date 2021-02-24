# shopping_cart.py
import os
import datetime
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#from dotenv import load_dotenv
#...
load_dotenv()  # take environment variables from .env.

TAX_RATE = os.getenv("TAX_RATE", default=0.0875)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)


#Info Inputs

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier or 'DONE' if there are no more items: ") #>string version of numbers
    
    if selected_id == "DONE":
        break
    else:
        #matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
        #matching_product = matching_product[0]
        #
        #total_price = total_price + matching_product["price"]
        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
        selected_ids.append(selected_id)
#print(selected_ids)

#print("TOTAL PRICE: " + str(total_price))

print("---------------------------------")
print("ANGEL FOODS GROCERY")
print("WWW.ANGEL-FOODS-GROCERY.COM")
print("3700 O St, NW, Washington DC")
print("202-968-2062")
print("---------------------------------")
#print("CHECKOUT AT: 2021-02-24 03:54 PM")



print("CHECKOUT AT: " + str(datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")))
print("---------------------------------")
print("SELECTED PRODUCTS:")


for selected_id in selected_ids:
        matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_product[0]
        
        total_price = total_price + matching_product["price"]
        print("... " + matching_product["name"] + " " + "("+str("${:,.2f}".format(matching_product["price"]))+")")

#> ---------------------------------
#> ANGEL FOODS GROCERY
#> WWW.ANGEL-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2021-02-24 03:54 PM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------
#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------
print("---------------------------------")

print("SUBTOTAL: " + "("+str("${:,.2f}".format(total_price))+")")

tc = int(total_price)*float(TAX_RATE)

print("TAX: " + "("+str("${:,.2f}".format(tc))+")")
print("TOTAL: " + "("+str("${:,.2f}".format(round(total_price+tc, 2)))+")")
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
#tax_calculation = int(total_price)
#print("TAX: " + ((tax_calculation)*0.08))


load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

# this must match the test data structure
template_data = {
    "total_price_usd": "("+str("${:,.2f}".format(round(total_price+tc, 2)))+")",
    "human_friendly_timestamp": str(datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"))
} # or construct this dictionary dynamically based on the results of some other process :-D

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))
#
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = template_data
print("MESSAGE:", type(message))

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)
