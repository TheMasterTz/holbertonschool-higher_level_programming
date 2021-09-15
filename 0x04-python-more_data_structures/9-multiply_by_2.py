def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items())

    for i, v in sorted_dictionary:
        print('{0}: {1}'.format(i, v))

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    for i, v in b_dictionary.items():
        b_dictionary[i] = v * 2
    return b_dictionary

new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)