# Gavin Mallott 47951130 and Yang Tang 53979886 ICS 31 Lab sec 1. Lab asst 6.
# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 e:  Remove all restaurants from the collection
 c:  Change the price of the dish served
 s:  Search the collection for selected restaurants
 d:  Search the collection for selected dishes
 v:  Print all restaurants under a specific average price
 w:  Print all restaurants of a specific price and cuisine
 p:  Print all the restaurants
 q:  Quit
>    """

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response == 'e':
            C = e()
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response == 'c':
            r = input("Please enter the name of the restaurant to change:  ")
            d = input("Please enter the dish you want to change:  ")
            p = input("Enter the percent to increase by:  ")
            C = Collection_change_price(C, r, d, p)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response == "w":
            print(Collection_str(Collection_return_selected(C)))
        elif response == 'v':
            p = int(input("Please enter the maximum average price:  "))
            print(Collection_str(Collection_select_cheap(C, p)))
        elif response == "d":
            name = input("Please enter the name of the dish you are searching for:  ")
            print(Collection_str(Collection_search_name(C, name)))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")

def e()->None:
    C = Collection_new()
    return C
   

##### Dishes
from collections import namedtuple
Dish = namedtuple("Dish", "name price calories")

def dish_str(n:Dish):
    """ Given a dish, prints the values of the dish as a string
    """
    return (n.name + " $" + str(n.price) + " " + str(n.calories) + " cal")

def dish_get_info() -> Dish:
    """ Prompt user for fields of a dish; create and return.
    """
    return Dish(input("Please enter the dish's name:  "),
                float(input("Please enter the price of the dish:  ")),
                int(input("Please enter the number of calories of the dish:  ")))

def dishlist_avg(n:list)->float:
    """ Given a list of dishes, returns the average price of all the dishes
    """
    all_prices = dishlist_prices(n)
    return sum(all_prices)/len(all_prices)

def dishlist_prices(n: list) -> list:
    """ Given a list of dishes, returns a list of the prices
    """
    return [dish.price for dish in n]

def dishlist_avg_cal(n:list)->float:
    """ Given a list of dishes, returns the average calories of all the dishes
    """
    all_cal = dishlist_cal(n)
    return sum(all_cal)/len(all_cal)

def dishlist_cal(n: list) -> list:
    """ Given a list of dishes, returns a list of the calories
    """
    return [dish.calories for dish in n]


##### Menus
def menu_enter():
    menu = []
    while True:
        command = input("Do you want to add a dish to the menu?  ")
        if command == "yes":
            menu.append(dish_get_info())
        elif command == "no":
            break
        else:
            invalid_command(command)
    return menu


##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', ['Escargots', 23.50, 250])

def Restaurant_str(self: Restaurant) -> str:
    menu = [dish_str(dish) for dish in self.menu]
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + "\n" + "\n".join(menu) + "\n" +
        "Average Cost: {}  Average Calories: {}".format(dishlist_avg(self.menu), dishlist_avg_cal(self.menu)) + "\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    name = input("Please enter the restaurant's name:  ")
    cuisine = input("Please enter the kind of food served:  ")
    phone = input("Please enter the phone number:  ")
    menu = menu_enter()
    return Restaurant(name, cuisine, phone, menu)

def Restaurant_is_cheap(n:namedtuple, p:float)->bool:
    """ Given a restaurat, returns true if the average price of all its dishes is lower than float p
    """
    avg = dishlist_avg(n.menu)
    if avg <= p:
        return True
    else:
        return False


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result

def Collection_change_price(C: list, rest: str, d: str, p: float) -> list:
    """ Given a list of restaurants, changes the price of each dish by percent p
    """
    result = []
    for r in C:
        if r.name == rest:
            for dish in r.menu:
                if dish.name == d:
                    for x, d in enumerate(r.menu):
                        new_price = d.price * (1 + (int(p)/100))
                        d = d._replace(price = new_price)
                        r.menu[x] = d
        result.append(r)
    return result

def Collection_select_cheap(C:list, n: float)->list:
    """ Given a list of restaurants, returns a list of restaurants if their average price is lower than float n
    """
    result = []
    for rest in C:
        if Restaurant_is_cheap(rest, n) == True:
            result.append(rest)
    return result

def Collection_select_cuisine(C:list, cuisine:str) -> list:
    """ Given a list of restaurants, returns a list of restuarants of the given cuisine
    """
    return [r for r in C if r.cuisine == cuisine]

def Collection_return_selected(C:list) -> list:
    """ Given a list of restaurants,
        returns a list of all restuarants with the given price and cuisine
    """
    p = int(input("Please enter the maximum average price:  "))
    c = input("Please enter preferred cuisine:  ")
    cheap = Collection_select_cheap(C, p)
    cuisine = Collection_select_cuisine(C, c)
    result = []
    for r in cheap:
        for rc in cuisine:
            if r == rc:
                result.append(r)
    return result

def Collection_search_name(C:list, name:str) -> list:
    """ Given a list of restaurants, returns a list of all restaurants containing name
    """
    restaurants = []
    for r in C:
        for dish in r.menu:
            if name in dish.name:
                restaurants.append(r)
    return restaurants

restaurants()
