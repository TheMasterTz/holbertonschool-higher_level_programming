#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Newlist = []
    for i in range(list_length):
        try:
            Newlist.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            Newlist.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            Newlist.append(0)
            print("division by 0")
            continue
        except IndexError:
            Newlist.append(0)
            print("out of range")
            continue

        finally:
            pass
    return Newlist
