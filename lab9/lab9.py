#  Yang Tang 53979886 and Yilin Huang 31687105.  ICS 31 Lab sec 7.  Lab asst 9.

#----PART C---
##C
print('----------------Part C--------------------')
from random import *
from collections import namedtuple
NUMBER_OF_STUDENTS = 20
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  
print()
##C1
print('----------------part c.1--------------------')
def generate_answers()->str:
    """ Takes a string and returns random selected answer"""
    alphabet='ABCDE'
    answers=''
    for n in range(NUMBER_OF_QUESTIONS):
        answers+=choice(alphabet[:NUMBER_OF_CHOICES])
    return answers

ANSWERS = generate_answers()
print()
print()



##C2
print('----------------part c.2--------------------')
Student = namedtuple('Student', 'name answers')

def random_students() -> [Student]:
    '''takes a length of students and return a list of students'''
    result=[]
    for i in range(NUMBER_OF_STUDENTS):
        result.append(Student("Student " + str(i+1), generate_answers()))
    return result
print(random_students())
print()
print()
print()



##C3
print('----------------part c.3--------------------')
Student = namedtuple('Student', 'name answers scores total')
def random_students()->[Student]:
    """ Using global constants to generate random student list of namedtuples"""

    result=[]
    for i in range(NUMBER_OF_STUDENTS):
        answers = generate_answers()
        scores = []
        for j in range(NUMBER_OF_QUESTIONS):
            if answers[j] == ANSWERS[j]:
                scores.append(1)
            else:
                scores.append(0)
        result.append(Student("Student " + str(i+1), answers,scores,sum(scores)))
    return result
print(random_students())
print()
def Mean(S:list)->int:
    '''takes a list of students and return a number of average scores of the students'''
    m=0
    for i in S:
        m += i.total
    return m/len(S)

def student_total(student:'Student')->int:
    '''takes a student and return the total score field'''
    return student.total
L=random_students()
L.sort(key=student_total, reverse = True)
for i in range(10):
    print(L[i].name)
print('Mean score: '+str(Mean(L)))
print()
print()
print()



##C4
print('----------------part c.4--------------------')
def generate_weighted_student_answer(c:str)->str:
    """ takes a string and returns a string
    """
    aw='ABCD'
    bw=aw+c*randrange(0,NUMBER_OF_CHOICES*2)
    return choice(bw)

def generate_answers2()->str:
    """ Takes a string and returns random selected answer"""
    alphabet='ABCDE'
    answers=''
    for n in range(NUMBER_OF_QUESTIONS):
        ANSWERS2=choice(alphabet[:NUMBER_OF_CHOICES])
        answers+=generate_weighted_student_answer(choice(alphabet[:NUMBER_OF_CHOICES]))
    return answers

def random_students2()->[Student]:
    """ Using global constants to generate random student list of namedtuples"""
    result=[]
    for i in range(NUMBER_OF_STUDENTS):
        answers = generate_answers2()
        scores = []
        for j in range(NUMBER_OF_QUESTIONS):
            if answers[j] == ANSWERS[j]:
                scores.append(1)
            else:
                scores.append(0)
        result.append(Student("Student " + str(i+1), answers,scores,sum(scores)))
    return result
print(random_students2())
L2=random_students2()
L2.sort(key=student_total, reverse = True)
for i in range(10):
    print(L2[i].name)
print()
print()
print()



##C5
print('----------------part c.5--------------------')
def question_weights(students:[Student])->'list of number':
    '''takes a list of students and return a list of number which contains the numbers of
    incorrect students' number'''
    result=[]
    for i in range(NUMBER_OF_QUESTIONS):
        total=0
        for j in students:
            if j.scores[i] == 0:
                total+=1
        result.append(total)
    return result

QUESTION_WEIGHTS=question_weights(L2)

def student_weighted_score(Student:'namedtuple of student'):
    result=[]
    for i in range (NUMBER_OF_QUESTIONS):
        student_score = QUESTION_WEIGHTS[i]*Student.scores[i]/sum(QUESTION_WEIGHTS)
        result.append(student_score)
    Student=Student._replace(scores=result)
    Student=Student._replace(total=sum(result))
    return Student

def students_with_weighted_score(Stu: Student)->Student:
    '''takes a list of students and change every student's scores field to weithted score, then return a new list of students '''
    result = []
    for i in range(len(Stu)):
        result.append(student_weighted_score(Stu[i]))
    return result

L3=students_with_weighted_score(random_students2())
L3.sort(key=student_total, reverse = True)
for i in range(10):
    print(L3[i].name)


#----PART D---
##D.1a
print('----------------part d.1a--------------------')
def calculate_GPA(G:list)->float:
    '''Returns GPA from grades'''
    GPA=0
    for g in G:
        if g=='A':
            GPA+=4
        elif g=='B':
            GPA+=3
        elif g=='C':
            GPA+=2
        elif g=='D':
            GPA+=1
        elif g=='F':
            GPA+=0
    return GPA/len(G)
assert calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
print()



##D.1b
print('----------------part d.1b--------------------')
def calculate_GPA2(G: list) -> float:
    """ Returns GPA from grades using dict """
    dict = {"A":4, "A-": 3.7, "B+": 3.3, "B": 3.0,"B-": 2.7, "C+": 2.3, "C": 2.0,"C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
    GPA=0
    for g in G:
        GPA += (dict[g])
        score = GPA / len(G)
    return score   
assert calculate_GPA2(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
print()



##D.2
print('----------------part d.2--------------------')
def flatten_2D_list(table:list)->list:
    """ Takes 2D table and returns list"""
    l=[]
    for i in table:
        l.extend(i)
    return l
assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]
print()



##D.3a
print('----------------part d.3a--------------------')
L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']
def skip_every_third_item(l:list)->str:
    """ Skips every third item"""
    for i in l:
        p=l.index(i)
        if (p+1)%3!=0:
            print(i)
skip_every_third_item(L)
print()
print()
print()



##D.3b
print('----------------part d.3b--------------------')
def skip_every_nth_item(l:list,n:int)->str:
    """ Skips every nth item"""
    for i in l:
        p=l.index(i)
        if (p+1)%n!=0:
            print(i)
skip_every_nth_item(L,3)
print()
print()
print()



##D.4
##D.4a
print('----------------part d.4a--------------------')
work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(L:list) -> dict:
    """ Returns dict where every key is a name of an employee and the value is the number of days worked for a week"""
    workers = {}
    for n in L:
        if n== "Bob":
            workers[n] = L.count("Bob")
        if n == "Kyle":
            workers[n] = L.count("Kyle")
        if n == "Larry":
            workers[n] = L.count("Larry")
        if n == "Brenda":
            workers[n] = L.count("Brenda")
        if n == "Samantha":
            workers[n] = L.count("Samantha")
        if n == "Jane":
            workers[n] = L.count("Jane")
    return workers
print(tally_days_worked(work_week))
print()
print()
print()



##D.4b
print('----------------part d.4b--------------------')
workers=tally_days_worked(work_week)
hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50}

def pay_employees(d1,d2):
    """ determine how much each employee will be payed """
    for w in d2 and d2:
        print(w,'will be paid',d1[w]*8*d2[w],'for',d1[w]*8,'hours of work at $',d2[w],'per hour')
pay_employees(workers,hourly_wages)
print()
print()
print()



##D.5
print('----------------part d.5--------------------')
def reverse_dict(D: dict) -> dict:
    """ reverses the dict and returns a new one"""
    new_dict = {}
    for n,m in D.items():
        new_dict[m] = n
    return new_dict
print(reverse_dict(hourly_wages))
