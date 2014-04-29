###THE DISCRETE STRUCTURES GRADE CALCULATING PROGRAM###
import re

def current(hw,q,ex1,ex2):
    grade= (hw*.15 + q*.10 + ex1*.20 + ex2*.20)/65.0
    return grade

def letter(grade):
    if 0.0 <float(grade)< .600:
        your_grade= "F"
    if .600 <= float(grade) < .700:
        your_grade = "D"
    if .700 <= float(grade) < .800:
        your_grade = "C"
    if .800 <= float(grade) < .900:
        your_grade = "B"
    if .900 <= float(grade) <= 1.000:
        your_grade = "A"
    return your_grade



        
with open('Grades.txt', 'r') as file:
    mylist= file.readlines()
    #Strip all whitespace
    mylist = [i.rstrip() for i in mylist[0:]]
    #split the newly stripped list
    newlist= [i.split(',') for i in mylist[0:]]
    name= [i[0].strip() for i in newlist]
    hw= [i[1].strip() for i in newlist]
    q= [i[2].strip() for i in newlist]
    ex1= [i[3].strip() for i in newlist]
    ex2= [i[4].strip() for i in newlist]
    

    int_homework=map(float, hw)
    int_quiz=map(float, q)
    int_ex1=map(float, ex1)
    int_ex2=map(float, ex2)

    SCORES= zip(int_homework, int_quiz, int_ex1, int_ex2)

    GRADE_AS_OF_TODAY= [current(i[0], i[1], i[2], i[3]) for i in SCORES[0:]]

    LETTER_GRADES= [letter(i) for i in GRADE_AS_OF_TODAY[0:]]

def get_A(x):
    final=((x*65))
    if final < 55.0:
        return "Not Passible"
    else:
        return (90.0-final) / 35

def get_B(x):
    final=((x*65))
    if final < 45.0:
        return "Not Passible"
    else:
        return (80.0-final) / 35

def get_C(x):
    final=((x*65))
    if final < 35:
        return "Not Passible"
    else:
        return (70.0-final) / 35

def get_D(x):
    final=((x*65))
    if final < 25:
        return "Not Passible"
    else:
        you_need=(60.0-final)
        if you_need<0:
            you_need=0
        return you_need / 35

A=[get_A(i) for i in GRADE_AS_OF_TODAY]

B=[get_B(i) for i in GRADE_AS_OF_TODAY]

C=[get_C(i) for i in GRADE_AS_OF_TODAY]

D=[get_D(i) for i in GRADE_AS_OF_TODAY]

students=zip(name, hw, q, ex1, ex2, GRADE_AS_OF_TODAY, LETTER_GRADES, A, B, C, D)
ourstring=str(students).strip('[]')


m=open("GradeAnalysis.txt", "r+")
tuples = re.findall(r'\((.+?)\)', ourstring) # (.+?) to perform a non-greedy match - important!
m.write ('\n'.join(t for t in tuples))
m.close()
    
