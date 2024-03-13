" Importing class from the other python files"
from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
# created object from the class
main_menu = Menu()
main_money_machine = MoneyMachine()
main_coffee_maker = CoffeeMaker()
#A welcome message
print("*"*50)
print("Welcome to OOP Coffee Machine")
print("*"*50)
print("Resource Report")
main_coffee_maker.report() # Get a report of all resources.
print("*"*50)
avaliable_drinks = (main_menu.get_items().split("/"))[0:-1] # Get the resources name in a list
is_drink_selected = False # using to avoid user typo for entering a drink.
# Until avaliable drinks, in loop
while len(avaliable_drinks) > 0:
    # Checking if the user types a correct drink name in the list or not
    while not is_drink_selected:
        user_drink_selection = input(f"Please select one of available drinks{avaliable_drinks}:\n").lower()
        if user_drink_selection in avaliable_drinks: # if the drink is in the list, stop the loop
            is_drink_selected = True
        else:
            # if the drink is not in the list, a warning message.
            print("You haven't selected one of the valid drinks, try again!\n")
    # after get a valid drink name, asks payment of it.
    if main_money_machine.make_payment(main_menu.find_drink(user_drink_selection).cost):
        # after succed payment, deduct resource of the drink
        main_coffee_maker.make_coffee(main_menu.find_drink(user_drink_selection))
        is_drink_selected = False # ask for new drink.
    else:
        is_drink_selected = False # if the payment not succed then ask for new drink.
    for drink in avaliable_drinks:
    # Checking all drinks sufficency, if one of ingiredents of the drink not avaliable, \
    # delete it from the list.
        if not main_coffee_maker.is_resource_sufficient(main_menu.find_drink(drink)):
            avaliable_drinks.remove(drink)
# if run out all drinks, create a resource report
print("*"*50)
print("Resource Report")
main_coffee_maker.report()
print("*"*50)
# End_of_Line(EOF)