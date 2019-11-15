#  Yang Tang 53979886 and Zheheng Zhao 28066913.  ICS 31 Lab sec 7.  Lab assignment 7.
#Part C
print('---C---')
import random
def get_names(name):
    f=open(name,"r")
    result = []
    files = f.readlines()
    for i in files:
        result.append(i.split()[0])
    return result
def random_name():
    res = ""
    if random.randrange(1,3) == 1:
        res += random.choice(get_names("malenames.txt")).title() + " " +random.choice(get_names("surnames.txt")).title() 
    else:
        res += random.choice(get_names("femalenames.txt")).title() + " " +random.choice(get_names("surnames.txt")).title() 
    return res
random_name()

def random_names(n:int)->list:
    'returns a list of n strings'
    result = []
    for i in range(n):
        result.append(random_name())
    return result

print(random_names(10))
print()


#Part D
print('---D---')
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rotated(n:int):
    if n > 26:
        n = n%26
    front = ALPHABET[:n]
    end = ALPHABET[n:]
    return end + front

def Caesar_encrypt(a:str,n:int):
    '''return the encrypted message'''
    a=a.upper()
    table = a.maketrans(ALPHABET,rotated(n))
    return a.translate(table)
print(Caesar_encrypt('run whatever tests assure you that the function works correctly',5))

def Caesar_decrypt(a:str,n:int):
    '''return the orignal message'''
    table = a.maketrans(rotated(n),ALPHABET)
    return a.translate(table)

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

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rotated(n:int):
    if n > 26:
        n = n%26
    front = LETTERS[:n]
    end = LETTERS[n:]
    return end + front

def Caesar_break(message:str):
    'return the plaintext for c'
    result=[]
    L=[]
    s=''
    file=open('wordlist.txt')
    l=file.readlines()
    for i in l:
        L.append(i.replace('\n','').upper())
    for key in range(len(LETTERS)):
        table = message.maketrans(rotated(key),LETTERS)
        p=message.translate(table)
        p2=list_of_words((p).split())
        for w in p2:
            if w.upper() in L:
                s+=w+" "
    return s

        
print(Caesar_break('WZS BMFYJAJW! YJXYX FXXZWJ DTZ YMFY YMJ KZSHYNTS BTWPX HTWWJHYQD'))
print()



#Part E
print('---E---')
def copy_file(p:str):
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    lines = infile.readlines()
    n=0
    if p=='line numbers':
        while(n<len(lines)):
            for line in lines:
                n=n+1
                outfile.write(str("{:>5}".format(n))+':'+line)
    elif p=='gutenberg trim':
        housekeeping=False
        for line in infile:
            if '*** END' in line:
                break
            elif '*** START' in line:
                housekeeping=True
                countinue
            elif housekeeping:
                outfile.write(line)
    elif p=='statistics':
        for line in lines:
            outfile.write(line)
            if len(line) == 1:
                n=n+1
        all_characters = 0
        for string in lines:
            all_characters += len(string)
        average_characters = str(all_characters/len(lines))
        average_characters_nonempty = str(all_characters / (len(lines) - n))
        print("{} lines in the list".format(len(lines)))
        print("{} empty lines".format(n))
        print("{} average characters per line".format(average_characters))
        print("{} average characters per non-empty line".format(average_characters_nonempty))
    infile.close()
    outfile.close()

copy_file('statistics')

