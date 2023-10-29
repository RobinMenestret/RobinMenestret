# This file is an open source file wrote by Robin MENESTRET and permits to crypte or decrypte a password file.

import includes.imp_icon
from includes.alphabets import standard_alphabet
from includes.password_generator import generated_password

print("This is a random password of length {} : {}".format(12, generated_password(12, gender = "standard")))


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




