import random
from alphabets import standard_alphabet

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
        i = random.randint(0,len(standard_alphabet))
        return standard_alphabet[i]
    elif gender == "digit":
        i = random.randint(0, 9)
        return standard_alphabet[i]
    else :
        print("This alphabet does not exist or is not already implemented, please correct the code.")        
        

def generated_password(length:int, gender = "standard")->str:
    new_password = ""
    for i in range(length):
        new_password += random_char(gender)

    return new_password



if __name__ == "__main__":
    print("This is a random password of length {} : {}".format(12, generated_password(12, gender = "standard")))
