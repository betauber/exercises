def input_string_to_number(string_of_written_numbers):
    print(string_of_written_numbers)
    string_list = string_to_string_list(string_of_written_numbers)
    print(string_list)
    number_list = string_list_to_number_list(string_list)
    print(number_list)
    return list_to_number(number_list)


def string_to_string_list(string):
    return string.split(',')


def string_list_to_number_list(list_of_strings):
    numbers = {'eins': 1, 'zwei': 2, 'drei': 3}
    return [numbers[x] for x in list_of_strings]


def list_to_number(list_of_numbers):
    return int(''.join(map(str, list_of_numbers)))


input_string = 'eins,zwei,drei'
print(input_string_to_number(input_string))
