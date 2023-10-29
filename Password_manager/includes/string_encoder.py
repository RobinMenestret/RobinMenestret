from alphabets import *

alphabet = standard_alphabet

def encoded_char(char_to_encode:str, corresponding_password_char:str)->str:
    for key in alphabet.keys() :
        if alphabet[key] == char_to_encode :
            code_of_char_to_encode = key
        if alphabet[key] == corresponding_password_char :
            code_of_corresponding_password_char = key
    code_of_encoded_char = (code_of_char_to_encode + code_of_corresponding_password_char)%len(alphabet)
    encoded_char = alphabet[code_of_encoded_char]
    return encoded_char



def encoded_string(string_to_encode:str, password:str)->str:
    encoded_string = ""
    for character in range(len(string_to_encode)):
        encoded_string += encoded_char(string_to_encode[character], password[character%len(password)])
    return encoded_string

if __name__ == "__main__":
    print("This is an encoded string : " + encoded_string("Cette_phrase_est_encodee_!", "P@s5w0R|)"))

