#quantity is total quantity and price is unit price.
fruits ={
    'banana': {'quantity':120, 'price':5},
    'apple': {'quantity':120, 'price':12},
    'orange': {'quantity':80, 'price':8}}

def view_inventory(fruits):
    for item in fruits.items():
        print(item)

#using the my_dict['key'] = value method of dictionary, we can update the dictionary values.
def update_inventory(fruits):
    item_name = input("Enter the item name to update: ")
    if item_name in fruits:
        new_qty = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))
        fruits[item_name]['quantity'] = new_qty
        fruits[item_name]['price'] = new_price
        print(f"{item_name} updated successfully!")
    else:
        print("Item not found in inventory.")  

update_inventory(fruits)
view_inventory(fruits)
# if the quantity of any fruit become 0 then we can just update it to 0 in values, instead of removing the entire fruit - WHY? - cuz it will show which fruits we sell in our shops and out of stocks.
