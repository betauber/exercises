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
DOMMI'S SOLUTION
'''
#  Input prompt and variable
hobby_person = eval(input("--> "))
#  Created list because all of a sudden, it was demanded to
#  keep the order of the list in the output
hobby_list = []
'''
Condition if the value exceeds 255. It's not good to change the
exercises on the fly all the time. The text on the paper CLEARLY says
for values above 255 print "Schwimmen". Now this. Please keep in mind
that we got free CodeRunner attempts for this exercise, because it seems I 
was penalized by it in moodle.
'''
if hobby_person > 255:
    print("Keine Hobbies")
#  step-wise subtraction of 2**y for y in range(7, -1, -1) from Hobby-Wert
#  (hobby_person). I tried to figure it out to do it with range but didn't
#  have enough time. Can be done, though.
elif hobby_person == 0:
    hobby_list.append("Keine Hobbies")
else:
    if hobby_person <= 255 and hobby_person >= 128:  #  Intervall for 2**7
        #  Put item in list per object.append()
        hobby_list.append("Naehen")
        hobby_person -= 2**7
    if hobby_person < 128 and hobby_person >= 64:  #  Intervall for 2**6
        hobby_list.append ("Klavier spielen")
        hobby_person -= 2**6
    if hobby_person < 64 and hobby_person >= 32:  #  Intervall for 2**5
        hobby_list.append("Fussball spielen")
        hobby_person -= 2**5
    if hobby_person < 32 and hobby_person >= 16:  #  Intervall for 2**4
        hobby_list.append("Laufen")
        hobby_person -= 2**4
    if hobby_person < 16 and hobby_person >= 8:  #  Intervall for 2**3
        hobby_list.append("Kochen")
        hobby_person -= 2**3
    if hobby_person < 8 and hobby_person >= 4:  #  Intervall for 2**2
        hobby_list.append("Angeln")
        hobby_person -= 2**2
    if hobby_person < 4 and hobby_person >= 2:  #  Intervall for 2**1
        hobby_list.append("Brettspiele")
        hobby_person -= 2**1
    if hobby_person < 2 and hobby_person > 0:  #  Intervall for 2**0
        hobby_list.append("Schwimmen")
        hobby_person -= 2**0
#  len(list) counts the number of items in a list -->
#  hobby_list_len represents the start value for range()
hobby_list_len = len(hobby_list)
#  hobby_list_len - 1 because of the way range counts.
for i in range(hobby_list_len-1, -1, -1):
    print(hobby_list[i])
