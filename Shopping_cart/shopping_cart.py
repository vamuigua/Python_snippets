class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    #Empty Dictionary
    items_in_cart = {}
    #Initializing a Method for Customer_name
    def __init__(self, customer_name):
        self.customer_name = customer_name
    #Initialize a method for adding item to cart
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."
    #Initializing method for removing item in cart
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

#Adds the Customer_name
my_cart = ShoppingCart("Victor")
#Adds the item in the Cart
my_cart.add_item("Diamond", 1000)
#Removes item in the Cart
my_cart.remove_item("Diamond")
