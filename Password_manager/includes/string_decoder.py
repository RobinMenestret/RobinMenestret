from alphabets import *

alphabet = standard_alphabet

def decoded_char(encoded_char:str, corresponding_password_char:str)->str:
    for key in alphabet.keys() :
        if alphabet[key] == encoded_char :
            code_of_encoded_char = key
        if alphabet[key] == corresponding_password_char :
            code_of_corresponding_password_char = key
    code_of_decoded_char = (code_of_encoded_char - code_of_corresponding_password_char)%len(alphabet)
    decoded_char = alphabet[code_of_decoded_char]
    return decoded_char



def decoded_string(encoded_string:str, password:str)->str:
    decoded_string = ""
    for character in range(len(encoded_string)):
        decoded_string += decoded_char(encoded_string[character], password[character%len(password)])
    return decoded_string

if __name__ == "__main__":
    print("This is an decoded string : " + decoded_string("bSLyA_$gVzg6{As§)I[QGiAe6z", "P@s5w0R|)"))

