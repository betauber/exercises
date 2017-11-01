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

'''
Hard coded attempt at a solution. 
Test value 219. 
Programm stops prematurely.

--> 219
Naehen
Klavier spielen
27

'''
# Input prompt
hobby_person = eval(input("--> "))
if hobby_person > 255:
    print("Schwimmen")
else:
    if hobby_person <= 255 and hobby_person >= 128:
        print("Naehen")
        hobby_person -= 2**7
    if hobby_person < 128 and hobby_person >= 64:
        print ("Klavier spielen")
        hobby_person -= 2**6
    if hobby_person < 64 and hobby_person >= 32:
        print("Fußball spielen")
        hobby_person -= 2**5
    if hobby_person < 32 and hobby_person >= 16:
        print("Laufen")
        hobby_person -= 2**4
    if hobby_person < 16 and hobby_person >= 8:
        print("Kochen")
        hobby_person -= 2**3
    if hobby_person < 8 and hobby_person >= 4:
        print("Angeln")
        hobby_person -= 2**2
    if hobby_person < 4 and hobby_person >= 2:
        print("Brettspiele")
        hobby_person -= 2**1
    if hobby_person < 2 and hobby_person > 0:
        print("Schwimmen")
        hobby_person -= 2**0
print(hobby_person)
