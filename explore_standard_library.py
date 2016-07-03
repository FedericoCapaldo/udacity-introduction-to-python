from random import randint

def generate_random_list(n):
    my_list = []
    for x in range (1, n):
        my_list.append(randint(1,100))
    return my_list

def order_list(list_to_be_ordered):
    ordered_list = []
    while len(list_to_be_ordered) > 0:
        lowest = min(list_to_be_ordered)
        list_to_be_ordered.remove(lowest)
        ordered_list.append(lowest)

    return ordered_list

print order_list(generate_random_list(150))