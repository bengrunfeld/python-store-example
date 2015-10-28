"""Main runner file the runs the store"""

import products

def print_menu():
    """Prints main menu"""
    print '1. Make a new item'
    print '2. Output a list of items'
    print '3. Exit'
    print 'Make a choice: ',

def get_new_name():
    """Gets input from User for a new name"""

    print 'Type new item name: ',
    return raw_input()


def get_new_price():
    """Gets input from User for a new price"""

    print 'Type new item price: ',
    return raw_input()


def get_new_description():
    """Gets input from User for a new description"""

    print 'Type new item description: ',
    return raw_input()


def process_user_input(choice):
    """Chooses what to do based on User input"""
    if choice == '1':
        # Get User input for product details 
        prod_name = get_new_name()
        prod_price = get_new_price()
        prod_desc = get_new_description()
        
        # Instantiate the product object
        prod_obj = products.Product()
        prod_obj.create_product(prod_name, prod_price, prod_desc)
        return False 

    elif choice == '2':
        prod_obj = products.Product()
        prod_obj.list_products()
        return False 

    elif choice == '3':
        # User exits program
        print 'Goodbye!' 
        return True 

    else:
        print '!!! Invalid choice !!!'
        print '!!!  CHOOSE AGAIN  !!!'
        return False 

def run_main_app():
    """Runs the main loop"""

    exit = False

    # Takes input from User. Will not quit
    # program unless User chooses 'exit option' 
    while not exit:
        print_menu()
        user_choice = raw_input()
        exit = process_user_input(user_choice)

run_main_app()
