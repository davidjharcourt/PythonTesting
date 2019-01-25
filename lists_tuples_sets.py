my_variable = "hello"

grades = [77, 80, 90, 95, 100]

tuple_grades = (77, 80, 90, 95, 100, 105, 107, 108, 109) #immutable

set_grades = {77, 80, 90, 100, 100} # unique & unordered

grades.append(100)

#print(sum(grades)/len(grades))

#print(set_grades)

tuple_grades = tuple_grades + (100,) #must have the comma here
#print(tuple_grades)

grades[0] = 60 #assign index
#print(grades[0]) #index number

set_grades.add(60)
#print(set_grades)

## Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_lottery_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_lottery_numbers))
print(your_lottery_numbers.union(winning_lottery_numbers))
print(your_lottery_numbers.difference(winning_lottery_numbers))
