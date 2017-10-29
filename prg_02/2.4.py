hobbies = {1: 'Schwimmen', 2: 'Brett', 4: 'Angeln', 8: 'Kochen', 16: 'Laufen', 32: 'Fuss', 64: 'Klavier', 128: 'Naehen'}


def calc_hobbies(x):
    if x > 255:
        return [hobbies[1]]

    h = []
    for i in [2 ** y for y in range(7, -1, -1)]:
        if x / i >= 1:
            h.append(hobbies[i])
            x -= i
    return h


x = 36
print(x)
print(calc_hobbies(x))
                    