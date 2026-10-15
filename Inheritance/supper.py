# Parent Class
class Parent:
    def __init__(self):
        self.public = "This is Public"
        self._protected = "This is Protected"
        self.__private = "This is Private"

    def show_private(self):
        print("Private:", self.__private)


# Child Class
class Child(Parent):
    def __init__(self):
        super().__init__()   # Calls Parent class constructor

    def display(self):
        print("Public:", self.public)
        print("Protected:", self._protected)


# Creating object
obj = Child()

obj.display()
obj.show_private()