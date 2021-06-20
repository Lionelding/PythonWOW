# Class Attribute VS Instance Attribute
"""
1. About python namespace
2. Class attribute vs instance attribute
"""


# 1. Python namespace
def namespace_example():
    print('1. namespace example')

    # 1.1
    # It is a mapping from attribute names to objects. Usually, we need dot syntax to access the namespace.
    class MyClass:
        # No need for dot syntax
        class_var = 1

        def __init__(self, i_var):
            self.i_var = i_var

    # Here, we need to use dot syntax
    print(MyClass.class_var)

    # 1.2
    # When we try to access an attribute from an instance of a class,
    # the programs looks for the attribute in the instance namespace.
    # If it fails to find it, it going to look for it in the class namespace.
    foo = MyClass(2)
    print(foo.i_var)  # 2
    print(foo.class_var)  # 1

    # 1.3
    # Instance namespace has supremacy over class namespace
    print('skippedd')


# 2. Class Attribute
def class_attribute_example():
    print('2. class attribute example')

    class MyClass:
        class_var = 1

        def __init__(self, i_var):
            self.i_var = i_var

    # If a class attribute is set by accessing the class, it will override the value for all instances
    foo1 = MyClass(2)
    foo2 = MyClass(2)

    MyClass.class_var = 100
    print(foo1.class_var)  # 100
    print(foo2.class_var)  # 100

    # 2.1
    # If a class attribute is set by accesing the instance, it will only override the value for that instance
    foo1.class_var = 150
    print(foo1.class_var)  # 150
    print(foo2.class_var)  # 100

    # This is because the program adds a `class_var` attribute to `foo.__dict__` in the instance namespace
    print(foo1.__dict__)
    print(foo2.__dict__)

    # 2.2
    # What if the class attribute is mutable type? Answer: They will share the class attribute, which is problematic.
    class MyService:
        data = []

        def __init__(self, other_data):
            self.other_data = other_data

    s1 = MyService(['a', 'b'])
    s2 = MyService(['c', 'd'])

    s1.data.append('1000')
    print(s1.data)  # 1000
    print(s2.data)  # 1000

    # We can get around by doing this
    s1 = MyService(['a', 'b'])
    s2 = MyService(['c', 'd'])

    s1.data = ['1000']
    s1.data = ['1500']

    print(s1.data)  # 1000
    print(s2.data)  # 1500

    # This is working, but it is a potential issue for people who are not familiar with this.


def why_to_use_class_attribute():
    print('3. Why to use class attribute')

    # 3.1 Store a constant or a default value
    class Circle:
        pi = 3.14159

        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return Circle.pi * self.radius * self.radius

    c = Circle(10)
    print(Circle.pi)  # 3.14159
    print(c.pi)  # 3.14159
    print(c.area())  # 314.159

    # 3.2 Tracking all instances within a class
    class Student:
        school = []

        def __init__(self, name):
            self.name = name
            Student.school.append(self.name)

    student1 = Student('Tom')
    student2 = Student('Jerry')
    print(Student.school)  # ['Tom', 'Jerry']


def main():
    namespace_example()
    class_attribute_example()
    why_to_use_class_attribute()


if __name__ == '__main__':
    main()

# REF: https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
