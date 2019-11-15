# Gavin Mallott 47951130 and Yang Tang 53979886. ICS 31 Lab sec 7. Lab Assihnment 6.



##C
#c1
print('---c1---')
def contains(n:str,m:str)->bool:
    'return true if m ocuurs in n'
    return m in n
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
assert contains('apple', 'ppl')
assert not contains('hello', 'ol')
print()
#c2
print('---c2---')
def sentence_stats(s:str):
    'prints out these statistics about s'
    punct_string = '*.,?!:;"'
    remove_punct_table = str.maketrans(punct_string, len(punct_string) * ' ')
    nopunct = s.translate(remove_punct_table)
    print('Characters: '+str(len(s))+'\n'+\
          'Words: '+str(len(nopunct.split()))+'\n'+\
          'Average word length: '+str(len(nopunct.replace(' ',''))/len(nopunct.split()))+'\n\n')
sentence_stats('I love UCI')
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
print()
#c3
print('---c3---')
def initials(s:str)->str:
    'return the initials of s in all capital letters'
    string=''
    new_list = s.split(' ')
    for i in new_list:
        string=string+i[0].upper()
    return string        
assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'
print()
#d
print('---d---')
#d1
print('---d1---')
from random import randrange
for i in range(50):
    i=randrange(0,11) 
    print(i)
print()
for i in range(50):
    i=randrange(1,7)
    print(i)
print()
#d2
print('---d2---')
def roll2dice()->int:
    'return the number that reflects the random roll of two dice'
    i=randrange(1,7)
    n=randrange(1,7)
    return n+i
for m in range(50):
    print(roll2dice())
print()
#d3
print('---d3---')
def distribution_of_rolls(n:int):
    'print the distribution of the values of rolls'
    l=[]
    for m in range(n):
            l.append(roll2dice())
    i=1
    while(i<12):
        i=i+1
        print("{:>2}:{:>6} ({:>4}%) \t{}".format(i,l.count(i),l.count(i)/n*100,'*'*l.count(i)))
    print('-----------------------------')
    print('      ',n,' rolls')
distribution_of_rolls(200)
print()
#e
print('---e---')
#e1
print('---e1---')
def rotate_alphabet(key:int) -> str:
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    new_alphabet = []
    for x, letter in enumerate(alphabet):
        try:
            new_alphabet.append(alphabet[x+key])
        except IndexError:
            y = len(alphabet) - x
            key = key % 26
            new_alphabet.append(alphabet[0+key-y])
    return ''.join(new_alphabet)


def Caesar_encrypt(plaintext:str, key:int) -> str:
    """ Takes a plaintext string and shifts all the letters forward by the key
    """
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", rotate_alphabet(key))
    return plaintext.translate(table)

message = Caesar_encrypt("hi there", 29)
print(message)

def Caesar_decrypt(ciphertext:str, key:int) -> str:
    """ Takes a ciphertext string and decrypts it with the given key
    """
    table = str.maketrans(rotate_alphabet(key), 'abcdefghijklmnopqrstuvwxyz')
    return ciphertext.translate(table)

message = Caesar_decrypt(message, 3)
print(message)
print()

#f
print('---f---')
list_of_string=[ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]
print('---f1---')
def print_line_numbers(l:list):
    'print each string preceded by a line number'
    i=1
    while(i<len(l)+1):
        print(i,':',l[i-1])
        i=i+1    
print_line_numbers(list_of_string)
print()
print('---f2---')
def stats(l:list):
    """ Prints statistics for the inputed list
    """
    num_of_lines = len(l)
    empty_lines = ([string for string in l if string == ''])
    number_of_empty_lines = len(empty_lines)
    all_characters = 0
    for string in l:
        all_characters += len(string)
    average_characters = str(all_characters/len(l))
    average_characters_nonempty = str(all_characters / (len(l) - number_of_empty_lines))
    print("{} lines in the list".format(num_of_lines))
    print("{} empty lines".format(number_of_empty_lines))
    print("{} average characters per line".format(average_characters))
    print("{} average characters per non-empty line".format(average_characters_nonempty))

stats(list_of_string)
print()
print('---f3---')
def list_of_words(l:list)->list:
    'return a list of individual words with all white space and punctuation removed'
    l2=[]
    import string
    for w in l:
        punct_string = '*.,?!:;"'
        remove_punct_table = str.maketrans(punct_string, len(punct_string) * ' ')
        nopunct = w.translate(remove_punct_table)
        p=nopunct.split()
        l2.extend(p)
    return l2
print(list_of_words(list_of_string))

