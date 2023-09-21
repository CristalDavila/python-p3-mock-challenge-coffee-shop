from statistics import mean

class Coffee:
    def __init__(self, name):
        self.name = name
        self._name = None
        

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
            if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
                self._name = name
            else:
                raise Exception 
                

        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return mean([order.price for order in self.orders()])

# Coffee property name CHECK
# Returns the coffee's name CHECK
# Names must be of type str CHECK
# Names length must be greater or equal to 3 characters CHECK
# Should not be able to change after the coffee is instantiated WHAT THE FUCK
# hint: hasattr() GRRR BETTER HINTS PLZ

# PART DEUX
# Coffee orders() CHECK
# Returns a list of all orders for that coffee CHECK
# Orders must be of type Order CHECK
# Coffee customers()CHECK
# Returns a unique list of all customers who have ordered a particular coffee.CHECK
# Customers must be of type Customer CHECKKKKKKK

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

        @property
        def name(self):
            return self._name
        
        name.setter
        def name(self, name):
            if isinstance(name, str) and 1 <= len(name) <= 15:
                self._name = name
            
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, set_coffee, set_price):
        return Order(self, set_coffee, set_price)
    
# Customer is initialized with a name CHECK
# Customer property name CHECK
# Returns customer's name CHECK
# Names must be of type str CHECK
# Names must be between 1 and 15 characters, inclusive CHECK
# Should be able to change after the customer is instantiated

# part deeeuuuuxxx
# Customer orders() CHECK
# Returns a list of all orders for that customer CHECK
# Orders must be of type Order CHECK
# Customer coffees() CHECK
# Returns a unique list of all coffees a customer has ordered CHECK
# Coffees must be of type Coffee CHEQUE


class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

        @property
        def customer(self):
            return self._customer
        
        @customer.setter
        def customer (self, customer):
            if isinstance(customer, Customer):
                self._customer = customer

@property
def coffee(self):
    return self._coffee

@coffee.setter
def coffee(self, coffee):
    if isinstance(coffee, Coffee):
        self._coffee = coffee
    else:
        raise Exception
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price (self, price):
        if(
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")

        ):
            self._price = price
        else:
            raise Exception

        

#         Order __init__(self, customer, coffee, price) CHECK
# Order is initialized with a Customer instance, a Coffee instance, and a price CHECK
# Order property price CHECK
# Returns the price for the order CHECK
# Prices must be of type float CHECK
# Price must be a number between 1.0 and 10.0, inclusive CHECK
# Should not be able to change after the order is instantiated CHECK
# hint: hasattr() CHECK I THIIIINK

# part deux
# Order property customer CHECK
# Returns the customer object for that order CHECK
# Must be of type Customer CHECK
# Order property coffee CHECK
# Returns the coffee object for that order CHECK
# Must be of type Coffee CHECK

