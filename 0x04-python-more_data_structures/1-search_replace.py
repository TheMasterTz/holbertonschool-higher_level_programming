my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
def search_replace(my_list, search, replace):
    #return [replace if i == search else i for i in my_list]
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace


new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)