from abc import ABC, abstractmethod
import copy

class Person(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Teacher(Person):
    def __init__(self, name, course):
        self._name = name
        self._course = course

    def clone(self):
        return copy.deepcopy(self)
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_course(self):
        return self._course
    
    def set_course(self, course):
        self._course = course
        
    def display(self):
        print(f'Teacher Details\n Name: {self._name}\n Course: {self._course}\n')

class Student(Person):
    def __init__(self, name, teacher:Teacher) -> None:
        self._name = name
        self._teacher = teacher
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_teacher(self):
        return self._name

    def set_teacher(self, teacher):
        self._teacher = teacher

    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        print(f'Student Details\n Name: {self._name}\n Course: {self._teacher.get_course()}\n Teacher:{self._teacher.get_name()}\n') 

# Client code
#----------Original Objects Creation----------------
teacher = Teacher('amulya', 'Design Patterns')
teacherCopy1 = teacher.clone()

student = Student('nikhil', teacherCopy1) #i'm using the teacher cloned object to pass to student
studentCopy1 = student.clone()

print("____First Entry____\n")
teacherCopy1.display()
studentCopy1.display()


#------Cloning From Original Objects----
"""
Insted of creating new objects for each new entry, 
we are cloning the previous object and modifying the attributes TO PASS SECOND ENTRY
"""
teacherCopy2 = teacher.clone()
teacherCopy2.set_name('vanaja')
teacherCopy2.set_course('Data Structures')

studentCopy2 = student.clone()
studentCopy2.set_name('steeve')
studentCopy2.set_teacher(teacherCopy2)

print('____Second Entry____\n')
teacherCopy2.display()
studentCopy2.display()


#Encapsulated cloning the teacher object and passing new entries
def register_teacher(name, course):
    teacherCopy = teacher.clone()
    teacherCopy.set_name(name)
    teacherCopy.set_course(course)
    return teacherCopy

#Encapsulated cloning the student object and passing new entries
def register_student(name, teacher:object):
    studentCopy = student.clone()
    studentCopy.set_name(name)
    studentCopy.set_teacher(teacher)
    return studentCopy

#----------create new teacher and student-------
t3 = register_teacher('neelima', 'High Level Design')
s3 = register_student('Prudhvi', t3)

print('____Third Entry____\n')
t3.display()
s3.display()

#----------create new teacher and student-------
t4 = register_teacher('sailu', 'c++')
s4 = register_student('rogers', t4)

print('____Fourth Entry____\n')
t4.display()
s4.display()
