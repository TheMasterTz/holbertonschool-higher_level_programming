def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items())

    for i, v in sorted_dictionary:
        print('{0}: {1}'.format(i, v))
        
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)