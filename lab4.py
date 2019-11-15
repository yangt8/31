# Yang Tang 53979886 and Beatrice Cheung 20665078.ICS 31 Lab 4. Section 2
#c
#c1
def test_number(n:int,s:str)->str:
    "input a number and a string to return true or false"
    if s == "even":
        return n%2 == 0
    elif s == 'odd':
        return n%2 != 0
    elif s=="positive":
        return n>0
    elif s=="negative":
        return n<0
   
        
assert test_number(14, 'even') == True
assert not test_number(100, 'odd') == True
assert test_number(33, 'positive') == True
assert not test_number(100, 'negative') == True
print()

#c2
def display()->str:
    "enter any word and print them out"
    return input("Enter a word:")
for c in display():
    print(c)
print()

#c3
def square_list(l:list)->int:
    "return the integers in the list **2"
    for i in l:
        print(i**2)
square_list([2, 3, 4, 10])
print()

#c4
def match_first_letter(c:str,l:list)->str:
    "return to the strings whose first character is the letter"
    for f in l:
        if c==f[0]:
            print(f)
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])
print()

#c5
def match_area_code(n:list,l:list)->str:
    "return the phone number whose are code in on the list of area codes"
    for t in l:
        for m in n:
            if t[1:4]==m:
                print('('+m+')'+t[5:])
match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])
print()

#c6 ###
def matching_area_code(n:list,l:list)->list:
    "return the phone number in a list whose are code in on the list of area codes"
    empty_list=[]
    for t in l:
        for m in n:
            if t[1:4]==m:
                empty_list.append('('+m+')'+t[5:])
    return empty_list
assert matching_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']) == ['(714)824-1234', '(949)555-1234']
print()

#d
#d1
vowel=['a','e','i','o','u','A','E','I','O','U']
"take a letter if it is a vowel sound"
def is_vowel(n:str)->bool:
    return n in vowel
assert is_vowel('u')==True
assert is_vowel('d')==False
assert is_vowel('a')==True
assert is_vowel('A')==True
print()

#d2
def print_nonvowels(c:str)->str:
    'print all the nonvowels in the word'
    for i in c:
        if is_vowel(i)==False:
            print(i)
print_nonvowels('apple')
print_nonvowels('love')
print()

#d3

def nonvowels(n:str)->str:
    'returns string of nonvowels'
    result=''
    for i in n:
        if not is_vowel(i):
            result += i
    return result
assert nonvowels('apple')=='ppl'
assert nonvowels('love')=='lv'
assert nonvowels('hello!')=='hll!'


def double(n:float)->float:
    'input a number than double it'
    return n*2
assert double(0) == 0
assert double(17.5) == 35
assert double(-223344) == -446688
print()

#d4
def consonants(s:str)->str:
    'returns string of consonants'
    n='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result=''
    for i in s:
        if i in n:
            result += i
    return result
assert consonants(' apple ')=='ppl'
assert consonants('hello!') == 'hll'

#d5
def isvowels(n:str)->str:
    'returns string of vowels'
    result=''
    for i in n:
        if is_vowel(i):
            result += i
    return result
assert isvowels('apple')=='ae'
assert isvowels('love')=='oe'
assert isvowels('hello!')=='eo'

def select_letters(s1: str, s2: str) -> str:
    'input two strings then returns a string containing either all vowels or all'
    'consonants'
    if s1=='v':
        return isvowels(s2)
    elif s1=='c': 
        return consonants(s2)
    else:
        return ''
assert select_letters('v', 'facetiously')=='aeiou'
assert select_letters('c', 'facetiously')=='fctsly'
assert select_letters('g', 'facetiously')==''

#d6
def hide_vowels(s:str)->str:
    'replaces vowels with hyphens'
    result=''
    for l in s:
        if is_vowel(l):
            result+='-'
        else:
            result+=l
    return result
assert hide_vowels('apple') == '-ppl-'
assert hide_vowels('love') == 'l-v-'
assert hide_vowels('hello!') == 'h-ll-!'

#e
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
R1=Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50)
def Restaurant_change_price(r:"Restaurant",n:float)->"Restaurant" :
    'returns the same object except the price which been added the number '
    return r._replace(price=n+r.price)
assert Restaurant_change_price(R1,5) == Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', dish='Mee Krob', price=17.5)
print()

#f
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish
R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 
RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]
#f1
def alphabetical(R:list)->list:
    'return a list in alphabetical order by name'
    return sorted(R)
print()
#f2
def alphabetical_names(R:list)->list:
    "returns a list of restaurants' name order in alphabetical order by name"
    l=[]
    for r in sorted(R):
        l.append(r.name)
    return l
print()
#f3
def all_Thai(R:list)->list:
    'returns all the restaurants whose cuisine is Thai'
    l1=[]
    for r in R:
        if r.cuisine=='Thai':
            l1.append(r)
    return l1                
print()
#f4
def select_cuisine(R:list,c:str)->list:
    'return all the restaurants that serves the specific cuisine'
    l2=[]
    for r in R:
        if r.cuisine==c:
           l2.append(r)
    return l2         
print()
#f5
def select_cheaper(R:list,n:float)->list:
    'return the restaurants whose price is less than the specified number'
    l3=[]
    for r in R:
        if r.price<n:
            l3.append(r)
    return l3           
print()
#f6
def average_price(R:list)->float:
    'returns the average price of those restaurants'
    l4=[]
    for r in R:
        l4.append(r.price)
    return sum(l4)/len(l4)
print()
#f7
print(average_price(select_cuisine(RL,'Indian')))
print()
#f8
print(average_price(select_cuisine(RL, 'Chinese')+select_cuisine(RL, 'Thai')))
print()
#f9
print(alphabetical_names(select_cheaper(RL,15.00)))
print()
#g
import tkinter
my_window=tkinter.Tk()
my_canvas=tkinter.Canvas(my_window,width=1000,height=1000)
my_canvas.pack()
def create_rectangle_from_center(x,y,h,w):
    my_canvas.create_rectangle(x-w/2,y-h/2,x+w/2,y+h/2)
create_rectangle_from_center(500,500,400,500)
tkinter.mainloop()










