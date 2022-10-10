#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    while True:
        try:
            if i < list_length:
                z = (my_list_1[i]/my_list_2[i])
                result.append(z)
                i += 1
            else:
                return result
            except IndexError:
                result.append(0)
                print("out of range")
                i += 1
            except TypeError:
                result.append(0)
                print("wrong type")
                i += 1
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
                i += 1
            finally:
                pass
