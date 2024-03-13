" This is Coffe Maker class. "
class CoffeeMaker:
    """ Models the machine that makes the coffee """
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """ Prints a report of all resources. """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """ Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for items in drink.ingredients:
            if drink.ingredients[items] > self.resources[items]:
                print(f"Sorry there is not enough {items}, for {drink.name} !")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """ Deducts the required ingredients from the resources. """
        for items in order.ingredients:
            self.resources[items] -= order.ingredients[items]
        print(f"Here is your {order.name} ☕️. Enjoy!")
