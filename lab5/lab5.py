# Dachelle Alo 72009721 and Yang Tang 53979886. ICS 31 Lab sec 2. Lab asst 5.

#
#
#   Part C
#
#
print('------ Part C -----')
print('\n')

#C1
print('------C1------')
from collections import namedtuple

Dish = namedtuple('Dish', 'name price calories')

d1=Dish('Paht Woon Sen',9.50,330)
d2=Dish('Whopper',10.00,330)
d3=Dish('Paht Woon Sen',9.50,330)
d4=Dish('Tandoori Chicken',13.50,250)
d5=Dish('Peking Duck',24.50,325)
d6=Dish('Mussamun',9.00,315)
d7 = Dish("Egg Foo Young", 8.50, 259)
d8 = Dish("Pastrami Sandwich", 11.50,249)
d9 = Dish("Natto Temaki", 5.50,105)
d10=Dish('Escargots',24.50,143)
d11=Dish("Ris de Veau",48.40,543)
d12=Dish('Bouillabaisse',32.00,332)
d13=Dish('Mee Krob',10.95,234)
d14 = Dish("Mussamun", 9.00,123)
d15 = Dish("Big Mac", 3.95,365)
d16 = Dish("Mahi Mahi Burrito", 7.50,623)
d17 = Dish("Cheeseburger", 2.50,263)
d18 = Dish("Hot Link Burger", 4.50,275)
d19 = Dish("Combo Pizza", 12.95,253)
d20 = Dish("Rogan Josh", 12.50,433)
d21 = Dish("Tandoori Chicken", 13.50,163)
d22 = Dish("Peking Duck", 24.50,389)
d23 = Dish("Grilled Duck Breast", 25.00,240)
d24 = Dish("Striped Bass", 24.50,347)
d25 = Dish("Cedar Plank Salmon", 21.50,205)

#C2
print('------C2------')
def Dish_str(d: Dish) -> str:
    '''returns a string in a special form'''
    return str(d.name) + ' ($' + str(d.price) + '): ' + str(d.calories) + ' cal'
assert Dish_str(d1)=='Paht Woon Sen ($9.5): 330 cal'
assert Dish_str(d2) == 'Whopper ($10.0): 330 cal'

#C3
print('------C3------')
def Dish_same(d:Dish, p:Dish)->bool:
    'return true if the names and the calories of D1 and D2 are equel'
    if d.name==p.name and d.calories==p.calories:
        return True
    else:
        return False   
assert Dish_same(d1,d2)== False
assert Dish_same(d1,d3)== True

###C4
print('------C4------')
def Dish_change_price(d:Dish, n:float) -> Dish:
    'return the dish with the price change of n'
    return d._replace(price=d.price + (d.price*n/100))
assert Dish_change_price(d1,50) == Dish(name='Paht Woon Sen', price=14.25, calories=330)
assert Dish_change_price(d2,75) == Dish(name='Whopper', price=17.5, calories=330)

#C5
print('------C5------')
def Dish_is_cheap(d: Dish, n: float) -> bool:
    '''returns True if d.price is less than n'''
    return d.price < n
assert Dish_is_cheap(d1, 10)
assert not Dish_is_cheap(d1, 9)

##C6
print('------C6------')
DL=[d1,d2,d3,d4,d5]
print(len(DL))
print()
print(sorted(DL))
print()
DL.append(d6)
print(DL)
print()

DL2=[d10,d11,d12,d13]
DL.extend(DL2)
print(DL)
print()

def Dishlist_display(l:list)->str:
    'create a string with the dish into a readable form'
    i=0
    while i<len(l):
        print('Name:'+l[i].name+'\n'+\
              'Price:'+str(l[i].price)+'\n'+\
              'Calories:'+str(l[i].calories)+'\n\n')
        i=i+1
Dishlist_display(DL)
print()

###C7
print('------C7------')
def Dishlist_all_cheap(d: DL, n: float) -> bool:
    '''returns True if the price of every dish on the list is less than n'''
    f=True
    for dish in d:
        if not Dish_is_cheap(dish,n):
            f=False
            break
    return f
print(Dishlist_all_cheap(DL,20))
print()

#C8
print('------C8------')
def Dishlist_change_price(l:list,n:float)->list:
    '''return each dish with the price change of n'''
    result=[]
    for d in l:
        d=d._replace(price=d.price+d.price*n/100)
        result.append(d)
    return result
print(Dishlist_change_price(DL,50))
print()

#C9
print('------C9------')
def Dishlist_prices(L: 'list of Dish') -> list:
    '''returns a list of the prices in list L'''
    price = []
    for x in L:
        price.append(x.price)
    return price
assert Dishlist_prices(DL) == [9.5, 10.0, 9.5, 13.5, 24.5, 9.0, 24.5, 48.4, 32.0, 10.95]

#C10
print('------C10------')
def Dishlist_average(L:list)->float:
    'return the average price of l'
    L2=Dishlist_prices(L)
    return sum(L2)/len(L2)
assert Dishlist_average(DL) == 19.185
print()

#c11
print('------C11------')
def Dishlist_keep_cheap(L: 'list of Dish', n: int) -> list:
    '''returns a list of dishes in L whose price is less than n'''
    cheap = []
    for x in L:
        if x.price < n:
            cheap.append(x)
    return cheap
assert Dishlist_keep_cheap(DL, 10) == [Dish(name='Paht Woon Sen', price=9.5, calories=330), Dish(name='Paht Woon Sen', price=9.5, calories=330), Dish(name='Mussamun', price=9.0, calories=315)]
assert Dishlist_keep_cheap(DL, 15) == [Dish(name='Paht Woon Sen', price=9.5, calories=330), Dish(name='Whopper', price=10.0, calories=330), Dish(name='Paht Woon Sen', price=9.5, calories=330), Dish(name='Tandoori Chicken', price=13.5, calories=250), Dish(name='Mussamun', price=9.0, calories=315), Dish(name='Mee Krob', price=10.95, calories=234)]

#C12
print('------C12------')
BL=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25]
def before_and_after():
    n=float(input('Enter a number: '))
    print(Dishlist_display(BL))
    BL2=Dishlist_change_price(BL,n)
    print(Dishlist_display(BL2))
before_and_after()
print()

#
#
# Part E
#
#
print('------ Part E ------')
print('\n')

#e
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])	
#e1
print('---e1---')
r3 = Restaurant('Pascal', 'French', '940-753-0107', [Dish('escargots', 12.95, 250),
                                                     Dish('poached salmon', 18.50, 550),
                                                     Dish('rack of lamb', 24.00, 850),
                                                     Dish('marjolaine cake', 8.50, 950)])
print()

#e2
print('---e2---')
def Restaurant_first_dish_name(r:Restaurant)->str:
    "return the name of the first dish on restaurant's menu"
    return r.menu[0]
print(Restaurant_first_dish_name(r3))
print()

#e3
print('---e3---')
def Restaurant_is_cheap(r:Restaurant,n:float)->bool:
    "return true if the average price of the Restaurant's menu is less than or equal to n"
    if Dishlist_average(r[-1])<=n:
        return True
    else:
        return False
assert Restaurant_is_cheap(r3, 15) == False
print(Restaurant_is_cheap(r3,15))
print()

#e4
print('---e4---')
#e4(a)
print('---e4(a)---')
Collection=[r1,r2,r3]

def Dish_raise_price(d:Dish)->list:
    '''Raise the price of the given dish by $2.5 and return the whole dishlist'''
    return d._replace(price=d.price+2.5)

def Menu_raise_prices(l:list)->list:
    '''Change dishes' price and return the Menu with new price'''
    result=[]
    for d in l:
        result.append(Dish_raise_price(d))
    return result

def Restaurant_raise_price(r:Restaurant)->list:
    '''Return the restaurant with changed price'''
    return r._replace(menu=Menu_raise_prices(r.menu))

def Collection_raise_prices(C:list)->list:
    '''Return the collection with changed price'''
    result=[]
    for r in C:
        result.append(Restaurant_raise_price(r))
    return result
print(Collection_raise_prices(Collection))

#e4(b)
print('---e4(b)---')
def Dish_change_price(d:Dish,n:int)->list:
    '''Raise the price of the dish by specified percentage and return the whole dishlist'''
    return d._replace(price = d.price*n/100)

def Menu_change_prices(l:list,n:int)->list:
    '''Change dishes' price and return the Menu with new price'''
    result=[]
    for d in l:
        result.append(Dish_change_price(d,n))
    return result

def Restaurant_change_prices(r:Restaurant,n:int)->Restaurant:
    '''Return the restaurant with changed price'''
    return r._replace(menu=Menu_change_prices(r.menu,n))

def Collection_change_prices(C:list,n:int)->list:
    '''Return the collection with changed price'''
    result=[]
    for r in C:
        result.append(Restaurant_change_prices(r,n))
    return result

print(Collection_change_prices(Collection,5))
print()

#e5
print('---e5---')
def Restaurant_select_cheap(r:Restaurant,n:float)->Restaurant:
    if Dishlist_average(r[-1])<=n:
        return r

def Collection_select_cheap(C:Collection,n:float)->list:
    result=[]
    for r in C:
        result.append(Restaurant_select_cheap(r,n))
    return result
print(Collection_select_cheap(Collection,30))
print()
#
#
# Part F
#
#
print('------ Part F ------')
print('\n')
#f
print('---f---')
print()

#
#
# Part G
#
#
print('------ Part G ------')
print('\n')
#g
print('---g---')
from collections import namedtuple
Count=namedtuple('Count','letter number')
def letter_count(s:str,n:str)->list:
    'return counts of the letter in n in the string s'
    L=[]
    for r in n:
        sub=r
        N=s.count(sub)
        C=Count(r,N)
        L.append(C)
    return L
print(letter_count('The cabbage has baggage', 'abcd'))               
print()


















