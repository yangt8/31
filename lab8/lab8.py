
#-----PART C-----
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

#C1
print('---C1---')
def read_menu_with_count(f)->list:
    file=open(f,'r')
    lines=file.readlines()
    r=[]
    for line in lines:
        if len(line.split())==1:
            pass
        else:
            l=line.split()
            r.append(Dish(" ".join(l[0:-2]),float(l[-2].replace('$','')),int(l[-1])))
    file.close()
    print(r)
read_menu_with_count('menu1.txt')
read_menu_with_count('menu2.txt')
print()
#C2
print('---C2---')
def read_menu(f)->list:
    file=open(f,'r')
    lines=file.readlines()
    r=[]
    for line in lines:
        l=line.split()
        p=Dish(" ".join(l[0:-2]),float(l[-2].replace('$','')),int(l[-1]))
        r.append(p)
    file.close()
    print(r)
read_menu('menu3.txt')
print()

#C3
print('---D3---')
def write_menu(LD: 'list of Dish', file):
    outfile = open(file, 'w')
    outfile.write(str(len(LD))+'\n')
    for Dish in LD:
            outfile.write('{:25}\t${:1.2f}\t{:10}'.format(Dish.name, Dish.price, Dish.calories)+'\n')
    outfile.close()
print()


#-----PART D-----
Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
  
StudentBody = [sW, sX, sY, sZ]
#D1
print('---D1---')
def Students_at_level(l:list,c:str)->list:
    """ takes list and returns students at class level"""
    result=[]
    for s in l:
        if s.level==c:
            result.append(s)
    return result       
print(Students_at_level(StudentBody,'FR'))
print()

#D2
print('---D2---')
def Students_in_majors(l:list,i:list)->list:
    """ Takes a list of students and an list of majors and returns the list of students"""
    result=[]
    for s in l:
        if s.major in i:
            result.append(s)
    return result 
print()

#D3
print('---D3---')
def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
        number of c2 (and False otherwise)
    '''
    return c1.dept == c2.dept and c1.num == c2.num
def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
        means matching department name and course number) and False otherwise.
    '''
    result = False
    for a_course in SL:
        if Course_equals(c, a_course):
            result = True
    return result
def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
studylist (and False otherwise)
'''
    return Course_on_studylist(Course(department, coursenum, '', '', 0), S.studylist)

def Students_in_class(l:list,d:str,c:str)->list:
    """ Takes l dept and conum and returns a list of entroled in specific class"""
    result=[]
    for s in l:
        if Student_is_enrolled(s,d,c):
            result.append(s)
    return result
print(Students_in_class(StudentBody,'ICS','31'))       
print()
#D4
print('---D4---')
def Student_names(l:list)->list:
    """ Take a list of students and return just the names of the students"""
    result=[]
    for s in l:
        result.append(s.name)
    return result
print(Student_names(StudentBody))
print()
#D5
print('---D5---')
for s in StudentBody:
    if s.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        print(s)
print()

for s in StudentBody:
    if s.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        print(s.name)
print()

count = 0
for s in StudentBody:
    if s.major == "ICS":
        count += 1
print(count)
print()

new_list = []
for s in StudentBody:
    if s.level == "SR" and s.major == "ICS":
        new_list.append(s.name)
print(new_list)
print()

count = 0
for s in StudentBody:
    if s.level == "SR" and s.major == "ICS":
        count += 1
print(count)
print()

count = 0
for s in StudentBody:
    if s.level == "SR" and s.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        count += 1
print(count / 7,'%')
print()

count = 0
for s in StudentBody:
    if s.level == "FR" and s.major in ['CS','CSE','BIM','INFX','CGS','SE','ICS'] and ics31 in s.studylist:
        count += 1
print(count)
print()

unit_sum = 0
count = 0
for s in StudentBody:
    for s1 in s.studylist:
        if s.level == "FR" and ics31 in s.studylist:
            unit_sum +=s1.units
print(unit_sum / 4)
print()

