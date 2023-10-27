# This file is an open source file wrote by Robin MENESTRET and permits to crypte or decrypte a password file.

import random
import includes.imp_icon



def random_char(gender = "standard")->str:
    # this function return one random character in a choosen alphabet
    # There is several admissible alphabets :
    # - "complete" is for a the entire alphabet (don't use it if you don't know what you do) (WARNING : NOT IMPLEMENTED)
    # - "standard" is the most complete and acceptable alphabet.
    # - "digit" is for only digit characters
    # - ...
    # 
    # You can add any alphabet you want if you consider it usefull (based on utf-8) 
    gender = gender.lower()
    if gender == "standard":
        i = random.randint(0,93)
        i += 33
        if i in [44, 45, 46]:
            return random_char("standard")
        else :
            return chr(i)
    elif gender == "digit":
        i = random.randint(0, 9)
        return(str(i))
    else :
        print("This alphabet does not exist or is not already implemented, please correct the code.")        
        

def generated_password(length:int, gender = "standard")->str:
    new_password = ""
    for i in range(length):
        new_password += random_char(gender)

    return new_password


print("This is a random password of length {} : {}".format(12, generated_password(12, gender = "digit")))


def encode_char(char_to_encode:str, corresponding_password_char:str)->str:
    code_of_char_to_encode = ord(char_to_encode)
    code_of_corresponding_password_char = ord(corresponding_password_char)
    


def encode_string(string_to_encode:str, password:str)->str:
    encoded_string = ""
    for character in range(len(string_to_encode)):
        pass

def encode_list_of_password(file_path:str, password):
    with open(file_path, 'r') as f:
        doc_clear = f.read()
        doc_crypt = ""
        for letter in doc_clear :
            doc_crypt += ord(letter)
    print(doc_crypt)


def decode_list_of_password():
    pass














def construct_alphabet():
    for i in range(200):
        print(str(i) + ' : "'+ chr(i+33) + '",')


construct_alphabet()

standard_alphabet = {
    0  : "!",    1  : "€",    2  : "#",    3  : "$",    4  : "%",
    5  : "&",    6  : "£",    7  : "(",    8  : ")",    9  : "*", 
    10 : "+",    11 : "§",    12 : "{",    13 : "}",    14 : "~",
    15 : "0",    16 : "1",    17 : "2",    18 : "3",    19 : "4",
    20 : "5",    21 : "6",    22 : "7",    23 : "8",    24 : "9",
    27 : "<",    28 : "=",    29 : ">",    30 : "?",    31 : "@",
    32 : "A",    33 : "B",    34 : "C",    35 : "D",    36 : "E",
    37 : "F",    38 : "G",    39 : "H",    40 : "I",    41 : "J",
    42 : "K",    43 : "L",    44 : "M",    45 : "N",    46 : "O",
    47 : "P",    48 : "Q",    49 : "R",    50 : "S",    51 : "T",
    52 : "U",    53 : "V",    54 : "W",    55 : "X",    56 : "Y",
    57 : "Z",    58 : "[",    60 : "]",    61 : "^",    62 : "_",
    63 : "`",    64 : "a",    65 : "b",    66 : "c",    67 : "d",
    68 : "e",    69 : "f",    70 : "g",    71 : "h",    72 : "i",
    73 : "j",    74 : "k",    75 : "l",    76 : "m",    77 : "n",
    78 : "o",    79 : "p",    80 : "q",    81 : "r",    82 : "s",
    83 : "t",    84 : "u",    85 : "v",    86 : "w",    87 : "x",
    88 : "y",    89 : "z",
}


