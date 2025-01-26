#everything... strings, ints, lists, dicts, tuples, sets, and functions are objects
#you can create own objects using classes
#functions associated with instances of objects are known as methods

#methods look different than basic functions... basic functions look like function_name(object)... methods look like object.function_name()

class Student:


    def __init__(self, first, last, courses=None):
        
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
        
    
    def add_course(self, course):

        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already in {course}")

    def remove_course(self, course):

        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{self.first_name} {self.last_name} is not in {course}")

    
    def __len__(self):
        return len(self.courses)
    
    def __repr__(self) -> str:
        return f"Student('{self.first_name}', '{self.last_name}', {self.courses})"

    
    def __str__(self):

        return f"First name {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"
#As you can see in the line above we used the capitalize function on both the first and last names of the students which is possible because they are simply strings.
#We cannot however use this function on the courses object because it is a list. We use the map function to help use a function for strings on the courses of david.

    def find_in_file(self, file_name):
        f = open(file_name)
        return f
    
    def add_to_file(self, file_name):
        f_contents = self.find_in_file().readline()
        return f_contents
        

courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['c++', 'rails', "rust"]

david = Student("david", "steffes", courses_1)
john = Student("john", "smith", courses_2)

david.add_course('python')
david.remove_course('c++')

#when we say print(david) it prints david within the __str__(self): function
print(david)
print(repr(david))


david = Student("david", "steffes", ['python', 'rails', 'javascript'])



def sum_lists(list_1, list_2):
    list_3 = []
    for l, j in zip(list_1, list_2):
        list_3.append(l + j)
    return list_3

even = [0,2,4,6,8,10]
odd = [1,3,5,7,9,11]

print(sum_lists(even, odd))