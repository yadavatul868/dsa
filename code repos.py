import os
print(os.path.dirname(os.getcwd()))

class Employee:
    no_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@walmart.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('atul', 'yadav', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)


# calling a method - via instance vs via class
print(emp_1.fullname()) # via instance
print(Employee.fullname(emp_2)) # via class

# Class Variables

# emp_1.pay
# emp_1.apply_raise()
# emp_1.pay

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)

# Changing the class variable

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Trying to change the class variable via instance
emp_1.raise_amount = 1.06
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Trying to change the class variable using init method

# reload the class definition and then run code below
print(Employee.no_of_employee)

emp_1 = Employee('atul', 'yadav', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)

print(Employee.no_of_employee)

# classmethods and staticmethods


class Employee:
    no_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@walmart.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount =  amount


emp_1 = Employee('atul', 'yadav', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05)
# same as doing - Employee.raise_amount = 1.05
# also classmethods can be run via instances, result will be the same - emp_1.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)




class Employee:

    no_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@walmart.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount =  amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    


emp_1 = Employee('atul', 'yadav', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)


emp_str_1 = 'atul-yadav-50000'
emp_str_2 = 'Jane-Doe-60000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)
print(new_emp_1.last)
print(new_emp_1.pay)
print(new_emp_1.email)



class Employee:

    no_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@walmart.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount =  amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if (day.weekday()==5) or (day.weekday()==6):
            return False
        else:
            return True


emp_1 = Employee('atul', 'yadav', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)

import datetime
my_date = datetime.date(2023, 10, 2)
my_date

print(Employee.is_workday(my_date))




class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@walmart.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


###################################### DSA Revision ######################################

# BST
## Search
## Insertion
## Deletion

# Usage
## Implement SET
## Sort an array in aescending order


class BinarySearchTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if data > self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        # visit left
        if self.left:
            elements += self.left.in_order_traversal()

        # visit center
        elements.append(self.data)

        # visit right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):

        elements = []

        # visit left
        if self.left:
            return self.left.

        # visit center

        # visit right

        return elements.sum()

    
def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(100))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())





# Recurrsion

def find_sum(n):

    if n == 1:
        return 1
    else:
        return n +  find_sum(n-1)


# Properties in Python


class Student:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

student = Student("Atul Yadav", "Intermediate Python")

print(student.name)


class Student:
    def __init__(self, name, class_name):
        self._name = name
        self.class_name = class_name
        
    @property
    def name(self):
        self.standup()
        return self._name

    def standup(self):
        print('This class method is an example of doing stuff before getting the attribute')
    
student = Student("Atul Yadav", "Intermediate Python")

print(student.name)
print(student._name)

student._name = "Jane Doe"




























