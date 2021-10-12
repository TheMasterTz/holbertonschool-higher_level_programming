def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
filename = "my_file_0.txt"
nb_lines = number_of_lines(filename)
print("{} has {:d} lines".format(filename, nb_lines))
