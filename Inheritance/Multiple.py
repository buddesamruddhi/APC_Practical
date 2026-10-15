class Student:
    name = "Rahul"
    _marks = 85
    __rollno = 101
    def display_name(self):
        print("Name:", self.name)
    def _display_marks(self):
        print("Marks:", self._marks)
    def __display_rollno(self):
        print("Roll No:", self.__rollno)
    def show_rollno(self):
        self.__display_rollno()
class Sports:
    sport = "Cricket"
    def display_sports(self):
        print("Sports:", self.sport)
class Result(Student, Sports):
    def show_marks(self):
        print("Protected variable:", self._marks)
        self._display_marks()
    def display_result(self):
        print("Result: Pass")
s = Result()
s.display_name()
print("Public variable:", s.name)
s.show_marks()
s.show_rollno()
s.display_sports()
s.display_result()