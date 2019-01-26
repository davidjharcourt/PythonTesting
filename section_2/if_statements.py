# should_continue = True
# if should_continue == True:
#     print("Hello")
#
# known_people = ["Natalie", "David", "Yolande"]
# person = input ("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if (number % 2 == 0):
#             evens.append(number)
#     return evens
#     print(evens)

def who_do_you_know():
    # Ask the user for a list of people they know
    people = input("Enter a list of names you know, separated by commas:  ")
    # Split the string into a list
    #people_list = people.split(",")
    # Trim spaces from people
    # people_without_spaces = []
    # for person in people_list:
    #     people_without_spaces.append(person.strip())
    people_without_spaces = [person.strip() for person in people.split(",")]
    # Return that list
    return people_without_spaces

def ask_user():
    # Ask user for a name
    input_person = input("What name would you like to check? ")
    #See if their name is in the list of people they know
    # Print out that they know the person
    if input_person in who_do_you_know():
        print("You know {}!".format(input_person))
    else:
        print("You don't know {}".format(input_person))

ask_user()
