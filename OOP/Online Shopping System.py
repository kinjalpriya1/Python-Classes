class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print("Product class object is created")

class ShoppingCart():
    def __init__(self):
        self.cart = []

    def addProduct(self, product):
        self.cart.append(product)
        print(f"{product.name} is added to the cart.")

    def removeProduct(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"{product.name} removed")
        else:
            print(f"{product.name} not found")

    def cost(self):
        cost = 0
        for i in self.cart:
            cost += (i.price * i.quantity)
        print(f"Total cost: {cost}")
        return cost

bread = Product("bread", 4.00, 3)
eggs = Product("eggs", 5.00, 2)
cheese = Product("cheese", 6.00, 4)

shoppingCart = ShoppingCart()
shoppingCart.addProduct(bread)
shoppingCart.addProduct(eggs)
shoppingCart.addProduct(cheese)
shoppingCart.removeProduct(eggs)
shoppingCart.cost()
  