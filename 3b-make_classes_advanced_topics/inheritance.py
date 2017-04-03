class Parent(object):
    """ Parent Class """

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))

class Child(Parent):
    """ A Child class that inherits from Parent class """

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        super(Child, self).__init__(last_name, eye_color)
        self.number_of_toys = number_of_toys

    # Method Overriding
    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))
        print("Number of Toys - {}".format(self.number_of_toys))

biley_cyrus = Parent("Cyrus", "blue")
biley_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Brown", "20")
miley_cyrus.show_info()
