my_variable = "hello"

grades = [77,80,90,95,100]

tuple_grades = (77,80,90,95,100,105,107,108,109) #immutable

set_grades = {77,80,90,100,100} # unique & unordered

grades.append(100)

print(sum(grades)/len(grades))

print(set_grades)

tuple_grades = tuple_grades + (100,)

print(tuple_grades)
