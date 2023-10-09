# names = ["sara",  "ramin"]
# print(len(names))
# print(type(names))

# names[0] = "reza"
# print(names)


# names = ("sara",  "ramin")
# print(len(names))
# print(type(names))

# names[0] = "reza"  Error
# print(names)


# favorite_sports = {
#     'sara': "football",
#     'rozha':"tennis"
#     }

# print(f"rozha likes {favorite_sports['rozha']}")

# for item in favorite_sports:
#     print(item)
# for item in favorite_sports.values():
#     print(item)
# for item in favorite_sports.items():
#     print(item[0],item[1])
# for key, val in favorite_sports.items():
#     print(key, val)

# student = {
#     'id':1,
#     'name':'nikan',
#     'age':22
# }

# print(student['age'])


# my_dict = {
#     1:"b",
#     2:"c"
# }

# print(my_dict[1])

# my_dict = {
#     (1,2):"b",
#     (2,3):"c"
# }
# print(my_dict[(1,2)])
# my_dict["w"] = "wwwwww"

# print(my_dict)
# del my_dict["w"]
# print(my_dict)
# pip install colorama
from colorama import Fore, Back, Style

all_students = []
message = f"""
{Fore.GREEN+Back.RED}0 => {"exit,":>40}{Style.RESET_ALL}
1 => add new student,
2 => show all students,
3 => remove a student,
4 => search a student,
{Fore.BLUE+Back.GREEN}5 => {"update student's info":>40}{Style.RESET_ALL}
"""

while True:
    print(message)
    user_input = input('>>> ')
    if user_input == '0':
        print("bye")
        exit()
    elif user_input == '1':
        student = {}
        student['name'] = input("enter student's name:> ")
        student['family'] = input("enter student's family:> ")
        student['age'] = int(input("enter student's age:> "))
        student['course'] = input("enter student's course:> ")
        all_students.append(student)

    elif user_input == "2":
        print(all_students)

    elif user_input == '3':
        name = input("enter student's name:> ")
        for i in range(len(all_students)):
            if all_students[i]["name"] == name:
                del all_students[i]
                print("student removed.")
                break

    elif user_input == "4":
        name = input("enter student's name:> ")
        for i in range(len(all_students)):
            if all_students[i]["name"] == name:
                print(f"student's course {all_students[i]['course']}")
                break

    elif user_input == "5":
        name = input("enter student's name:> ")
        for i in range(len(all_students)):
            if all_students[i]["name"] == name:
                print("which one to update (`age` or `course`)")
                user_choice_key = input("> ")
                print(f"what do you want to set for {user_choice_key}")
                user_choice_val = input("> ")
                all_students[i][user_choice_key] = user_choice_val

                print(f"student's {user_choice_key} updated to {user_choice_val}")
                break
