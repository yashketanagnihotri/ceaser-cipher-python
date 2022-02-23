import os


def clearConsole():
    command = "clear"
    if os.name in ("nt", "cls"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
logo = (
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)
clearConsole()
print(logo)
direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def shift_letters(direction, text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
            else:
                new_position = position - shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    if direction == "encode":
        print(f"The encoded text is {cipher_text}")
    else:
        print(f"The decoded text is {cipher_text}")


while direction != "exit":
    if direction == "encode":
        shift_letters(direction, text, shift)
    elif direction == "decode":
        shift_letters(direction, text, shift)
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt ,type 'exit' for exiting :\n"
    )
    if direction == "exit":
        print("Thank you for using ceaser cipher, have a good day!!")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
