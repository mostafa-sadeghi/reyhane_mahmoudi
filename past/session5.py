# my_list = []
# total = 0
# for number in range(100, 251):
#     if number % 3 == 0:
#         my_list.append(number)
#         if number % 2 != 0:
#             total += number

# print(my_list)
# print(total)


# def my_func(name, family):

#     return f"hello {name} {family}"

# print(my_func("mary", "blalal"))
# print(my_func(family="blalal",name="mary"))


from ast import arg


def calc(*args):
    n1, n2, *n = arg
    n1, *n2, n3 = arg
    return (sum(args))


result = calc(2, 45, 3)
print(result)
result = calc()
print(result)


# def my_func(**kwargs):
#     return f"hello {kwargs['name']} {kwargs['family']}, welcome to {kwargs['course']} class"


# print(my_func(name="sara", family="rezaei", course="django"))
