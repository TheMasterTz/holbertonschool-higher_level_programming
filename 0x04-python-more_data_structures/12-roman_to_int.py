""" Roman to Integer test file
"""
def roman_to_int(roman_string):
    roman_number = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    num = 0
    last = 0
    for letter in roman_string:
        for element in roman_number:
            if letter == element[0]:
                if last == 0 or last >= element[1]:
                    num += element[1]
                elif last < element[1]:
                    num += element[1] - (last * 2)

                last = element[1]
    return num

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))