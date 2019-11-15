# Julia Jue 82346473 and Hailey Tang 53979886. ICS 31 Lab sec 7. Lab Asst 2.

#c
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)
#c1
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:  ','$', rate)
print('Weekly salary:  ','$', hours * rate)

#c2
name=input('Hello. What is your name?')
print('Alice Anteater')
print("It's nice to see you.")
age=input('How old are you?')
print('Next year you will be 20 years old.')
print('Good-bye!')

#d
krone_per_euro=7.46
pound_per_euro=8.60
dollar_per_euro=6.62
name=input('Business name: ')
number_of_euros=int(input('Number of euros: '))
number_of_pounds=int(input('Number of pounds: '))
number_of_dollars=int(input('Number of dollars: '))

print('Copenhagen Chamber of Commerce')
print('Business name:  ', name)
euros_amount=number_of_euros*krone_per_euro
pounds_amount=number_of_pounds*pound_per_euro
dollars_amount=number_of_dollars*dollar_per_euro
print(number_of_euros, 'euros is', euros_amount, 'krone')
print(number_of_pounds, 'pounds is',pounds_amount, 'krone')
print(number_of_dollars, 'dollars is', dollars_amount, 'krone')

print('Total krone: ', euros_amount+pounds_amount+dollars_amount)

#e
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

#e1
print(still_another.title)
#e2
print(another.price)
#e3
print((favorite.price + another.price + still_another.price)/ 3)
#e4
print(favorite.year < 1900)
#e5
still_another=still_another._replace(price=26)
print(still_another)
#e6
still_another=still_another._replace(price=25*1.2)
print(still_another)

#f
from collections import namedtuple
Animal = namedtuple ('Animal', 'name species age weight favorite_food')
A1 = Animal ('Jumbo', 'elephant', 50, 1000, 'peanuts')
A2 = Animal ('Perry', 'platypus', 7, 1.7, 'shrimp')
print (A1.weight>A2.weight)

#g
booklist = [favorite, another, still_another]
#g1
print(booklist[0]<booklist[1])
#g2
print(booklist[0]<booklist[-1])

#h
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
#h1
print(RC[2].name)
#h2
print(RC[0].cuisine == RC[3].cuisine)
#h3
print(RC[-1].price)
#h4
RC.sort()
print(RC)
#h5
RC.sort()
print(RC[-1].dish)
#h6
RC.sort()
first_two=[RC[0],RC[1]]
last_two=[RC[-2],RC[-1]]
first_two.extend(last_two)
print(first_two)

#i
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line

tkinter.mainloop()          # Combine all the elements and display the window

#i1,i2
import tkinter              
my_window = tkinter.Tk()    
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  
my_canvas.pack()           
my_canvas.create_rectangle(20, 20, 220, 220)
my_canvas.create_polygon(120, 20, 220, 120, 120, 220, 20, 120)
tkinter.mainloop()

#i3
import tkinter              
my_window = tkinter.Tk()    
my_canvas = tkinter.Canvas(my_window, width=800, height=800)  
my_canvas.pack()

my_canvas.create_polygon(200, 0, 400, 200, 0, 200)
my_canvas.create_rectangle(50, 200, 350, 600)
my_canvas.create_rectangle(70, 250, 90, 270)
my_canvas.create_rectangle(150, 350, 250, 600)
tkinter.mainloop()

#i4
import tkinter              
my_window = tkinter.Tk()    
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  
my_canvas.pack() 
my_canvas.create_oval(50, 100, 450, 300)
my_canvas.create_oval(150, 100, 350, 300, fill='brown')
my_canvas.create_oval(220, 170, 280, 230, fill='black')
tkinter.mainloop()

#i5 iphone
import tkinter
my_window= tkinter.Tk()
my_canvas= tkinter.Canvas(my_window, width=1000, height=1000)
my_canvas.pack()
my_canvas.create_rectangle(100, 100, 500, 800)
my_canvas.create_rectangle(150, 200, 450, 700, fill='black')
my_canvas.create_rectangle(250, 155, 350, 165, fill='gray')
my_canvas.create_oval(260, 710, 340, 790)
my_canvas.create_oval(230, 155, 240, 165, fill='black')
my_canvas.create_oval(295, 125, 305, 135, fill='black')
tkinter.mainloop()
