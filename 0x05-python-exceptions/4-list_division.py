#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    if list_length <= 0:
        print("out of range")
        return result
    while True:
        try:
            result.append(my_list_1[i]/my_list_2[i])
        except IndexError:
            result.append(0)
            print("out of range")
        except TypeError:
            result.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        finally:
            i += 1
