def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str(str_number[0]))

    if len(str_number) > 1:
        return first*get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits('0052080'))
print(get_multiplied_digits('00123'))
print(get_multiplied_digits('40203'))
