# lottery_player_dict = {
#     'name': 'Rolf',
#     'numbers': (5,9,12,3,1,21)
# }
#
# class LotteryPlayer:
#     def __init__(self, name):
#         self.name = name,
#         self.numbers = (5,9,12,3,1,21)
#     def total(self):
#         return sum(self.numbers)
#
# player_one = LotteryPlayer("Rolf")
# player_two = LotteryPlayer("John")
# print(player.name)
# print(player.numbers)
# print(player.total())

# print(player_one == player_two)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}.".format(self.school))

    @classmethod #pass class, not object
    def go_to_school_class(cls):
        print("I'm going to school.")
        print("I'm going to {}.".format(cls))

    @staticmethod
    def go_to_school_static():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
rolf = Student("Rolf","Oxford")
anna.marks.append(56)
anna.marks.append(58)

print(anna.marks)
print(anna.average())
anna.go_to_school()
Student.go_to_school_static()
