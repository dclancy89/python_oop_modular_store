from product import new_product
from store import new_store


# Product(price, item_name, weight, brand)
store1 = new_store("123 Sesame Street", "Daniel Clancy")

product1 = new_product(5, "Cookies", "16oz", "Oreo")
product2 = new_product(10, "Chicken", "2lbs", "Perdue")

print "adding products"
store1.add_product(product1).add_product(product2)

print "Inventory"
store1.inventory()


print "Removing a product"
store1.remove_product(product1)


print "Inventory"
store1.inventory()