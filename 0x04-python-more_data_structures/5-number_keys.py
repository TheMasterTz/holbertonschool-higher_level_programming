a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
def number_keys(a_dictionary):
    return len(a_dictionary.keys())

nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))