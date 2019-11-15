# Hailey and Andrew

print('hello')

print(123+456)

print(2**5)

print(5*4*3*2*1)

number_of_students=356
number_of_staff=16 
print(number_of_students/number_of_staff)


def factorial (n: int) -> int:
    ''' compute n! (n factorial) '''
    if n <=0:
        return 1
    else:
        return n * factorial(n-1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(10))
print("100! is", factorial(100))
print("120! is", factorial(120))
print("50*10! is", factorial(50*10))
print("factorial(5)! is", factorial(factorial(5)))

#IMPORTANT
print('the sum of the five integers from 2 to 10 is', 2+4+6+8+10)
averagepercent=((75+83.5+61+43)/4)

print('the average of this group of test scores is', averagepercent, '%')
print('2 to thr 10th power is', 2**10)
print('its kinetic energy is', 0.5*50*(15**2))

wall = 'w'
cannon = 'c'
print(wall+cannon)
print(wall+cannon+wall)
print(wall*3+cannon+wall*3)
print((wall+cannon*2)*4)
print((wall*3+cannon)*4+wall)
print((wall*4+cannon)*4+wall*4)


#IMPORTANT
test_scores = "4325220523455023"
print('quiz score for the 1st student is', (test_scores[0]))
print('quiz score for the 5th student is', (test_scores[4]))
print('quiz score for the 10th student is', (test_scores[9]))
print('quiz score for the 16th student is', (test_scores[15]))

s = "anteater"
print(s[0]=='a')
print(s[7]=='r')
print(s[3]=='x')
print(s[0+1+2]=='zot')
print(len(s)=='r')

print('pi = 3.13159')
print('make = "toyota"')
print('model = "camry"')
print('year = 2014')
print('a=(3+5+7+9)/4')

print(20+35 > 2**4)
print(10%3 <= 1)
print('hello !' == 'goodbye')
list=('apple','orange','banana','mango')
print(len(list)==5)



s = "abcdefghijklnmopqrstuvwxyz"
print(s[3]+s[14]+s[6])
print(s[19]+s[21])
print(s[8]+s[2]+s[18])
print(s[20]+s[2]+s[8])
