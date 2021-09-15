my_list = [1, 2, 3, 1, 4, 2, 5]
def uniq_add(my_list=[]):
    return sum(set(my_list))

result = uniq_add(my_list)
print("Result: {:d}".format(result))