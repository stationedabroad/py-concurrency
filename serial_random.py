import random

def fn(count, out_list, call_number):
    for i in range(count):
        out_list.append(random.random())
    print(f'Call: {call_number} --> {sum(out_list)}')
