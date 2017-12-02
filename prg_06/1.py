import numpy as np


def create_random_matrix(n=2, m=2):
    assert n >= 2 and m >= 2
    matrix = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[(i, j)] = random_integer()

    return matrix


def random_integer():
    return int(np.random.randint(1000))  # TODO


def add_specfic_numbers(matrix):
    matrix = set_random_one_digit(matrix)
    matrix = set_random_two_digit(matrix)
    matrix = set_random_three_digit(matrix)
    matrix = set_random_four_digit(matrix)

    return matrix


def set_random_one_digit(matrix, i=1, j=1):
    matrix[(i, j)] = np.random.randint(0, 10)
    return matrix


def set_random_two_digit(matrix, i=1, j=2):
    matrix[(i, j)] = np.random.randint(10, 100)
    return matrix


def set_random_three_digit(matrix, i=2, j=1):
    matrix[(i, j)] = np.random.randint(100, 1000)
    return matrix


def set_random_four_digit(matrix, i=2, j=2):
    matrix[(i, j)] = np.random.randint(1000, 10000)
    return matrix


def matrix_as_string(matrix, spacing_func, spacing_character=" ", n=2, m=2):
    matrix_str = ""
    for i in range(1, n + 1):
        matrix_str += "("
        for j in range(1, m + 1):
            matrix_str += spacing_func(matrix, i, j, spacing_character)
            matrix_str += str(matrix[(i, j)])
            matrix_str += spacing_character
        matrix_str = matrix_str.rstrip(spacing_character)
        matrix_str += ")\n"
    return matrix_str


def simple_spacing(matrix, i, j, spacing_character):
    return ""


def right_aligned_spacing(matrix, i, j, spacing_character):
    largest_digit = get_largest_digit_in_column(matrix, j)
    length_difference = calc_digit_length_difference(matrix[(i, j)], largest_digit)
    return spacing_character * length_difference


def calc_digit_length_difference(integer, longest_digit):
    digits_of_integer = int(len(str(integer)))
    return longest_digit - digits_of_integer


def get_largest_digit_in_column(matrix, column, n=2, m=2):
    assert column <= m
    longest_digit = 1
    for i in range(1, n + 1):
        digits_of_value = int(len(str(matrix[(i, column)])))
        if longest_digit < digits_of_value:
            longest_digit = digits_of_value
    return longest_digit


matrix = create_random_matrix()
matrix = add_specfic_numbers(matrix)
print(matrix)
print(matrix_as_string(matrix, simple_spacing, spacing_character=" "))
print(matrix_as_string(matrix, right_aligned_spacing, spacing_character=" "))
# print(right_aligned_spacing(matrix, 1, 1, '§'))
# print(right_aligned_spacing(matrix, 1, 2, '§'))