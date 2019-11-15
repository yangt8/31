# Dachelle Alo 72009721 and Yang Tang 53979886. ICS 31 Lab sec 2. Lab asst 5.

#----Part F------

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
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
 #           dish()
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='e':
            C=[]
        elif response=='c':
            n = float(input("Please enter the amount representing a percentage change in price:"))
            C=Collection_change_prices(C,n)
            
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")


from collections import namedtuple
Dish=namedtuple('Dish','name price calories')


def dish():  
    print('Do you want to add a Dish?')
    our_rests=Collection_new()
    our_rests = Menu_enter(our_rests)
    
def Menu_enter()->list:
    result = []
    while True:
        response=input("yes or no")
        if response=='yes':
            d=Dish_get_info()
           # D = Collection_dish_add(D,d)
            result.append(d)
           
        elif response=='no':
            break
            #print(Collection_dish_str(D))
    return result
##### Dish

def Dish_str(self: Dish) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Price:  " + str(self.price) + "\n" +
        "calories:    " + str(self.calories)+"\n\n")

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish( 
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter calories of that dish:  ")))

def Collection_dish_add(D: list, d:Dish) -> list:
    """ Return list of dishes with input dish added at end.
    """
    D.append(d)
    return D

def Collection_dish_str(D: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for d in D:
        s = s + Dish_str(d) +"\n"
    return s
########################################################################################################################


##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        Collection_dish_str(self.menu))
 #       "Dish:     " + self.dish + "\n" +
#        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())


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

def Collection_change_prices(C:list, n:float) -> list:
    'return list of restaurants with the change of price'
    result = [ ]
    for r in C:
        r2=r._replace(price=r.price+r.price*n/100)
        result.append(r2)
    return result

restaurants() 


