# -*- coding: utf-8 -*-

def calculator(last_name, second_name, name, birth_date, gender):
    vowel = ['a', 'e', 'i', 'o', 'u']
    curp = ''

    # First letter of last_name
    if last_name[0] == 'ñ':
        curp += "x"
    else:
        curp += last_name[0]

    # First vowel of last_name
    for letter in last_name:
        if letter in vowel:
            curp += letter
            break

    if second_name[0] == 'ñ':
        curp += "x"
    else:
        curp += second_name[0]

    if name[0] == 'ñ':
        curp += "x"
    else:
        curp += name[0]

    date = birth_date.split("/")

    curp += date[2][2:]
    curp += date[1]
    curp += date[0]
    curp += gender
    curp += "df"

    curp += get_consonant(last_name[2:])
    curp += get_consonant(second_name[1:])
    curp += get_consonant(name[1:])


    return curp


def get_consonant(str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in str:
        if i not in vowel:
            if i == 'ñ':
                return "x"
            else:
                return i
