
class Store(object):
	def __init__(self, location, owner):
		self.products = []
		self.location = location
		self.owner = owner

	def add_product(self, product):
		self.products.append(product)
		return self

	def remove_product(self, product):
		self.products.remove(product)
		return self

	def inventory(self):
		for product in self.products:
			print product.display_info()
			print " "
		return self

def new_store(location, owner):
	return Store(location, owner)


if __name__ == "__main__":
	store = Store('the moon', 'daniel')
	store.inventory()