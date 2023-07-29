from random import choice
import time
import timeit

# start_time = time.time()
code = """us = 'r'
ss = 'p'
if us == 'r':
    if ss == 'p':
        print("system is the winner")
    elif ss == 's':
        print("user is the winner")
    else:
        print("equal")
elif us == 'p':
    if ss == 'r':
        print("user is the winner")
    elif ss == 's':
        print("syatem is the winner")
    else:
        print("equal")
elif us == 's':
    if ss == 'r':
        print("system is the winner")
    elif ss == 'p':
        print("user is the winner")
    else:
        print("equal")
"""

print(timeit.timeit(code, number=10000))

# print("duration:",time.time() - start_time)

"""
first exp with or clauses : 0.0010228157043457031



                            0.0011799335479736328
                            0.39613
"""




