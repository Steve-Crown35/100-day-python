alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_message = ""
    for i in text: 
        if i == " ":
            new_letter = "*"
            encrypted_message += new_letter 
        elif i == ".":
            new_letter = "~"
            encrypted_message += new_letter
        elif i == ",":
            new_letter = "`"
            encrypted_message += new_letter
        else:
            position = alphabet.index(i)
            new_position = position + shift
            new_letter = alphabet[new_position]
            encrypted_message += new_letter  
        
    print(f"the encoded message is : {encrypted_message}")

def decrypt(cipher_text, shift_amount):
    decrypted_message = ""
    for i in text:
        if i == "*":
            new_letter = " "
            decrypted_message += new_letter 
        elif i == "~":
            new_letter = "."
            decrypted_message += new_letter
        elif i == "`":
            new_letter = ","
            decrypted_message += new_letter
        else:
            position = alphabet.index(i)
            new_position = position - shift
            new_letter = alphabet[new_position]
            decrypted_message += new_letter  
        
    print(f"the decoded message is : {decrypted_message}")

'''if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(cipher_text = "text", shift_amount = shift)'''


def cipher(cipher_direction, start_text, shift_amount):
    if direction == "encode":
        encrypt(text = text, shift = shift)
    elif direction == "decode":
        decrypt(cipher_text = "text", shift_amount = shift)
        

cipher(cipher_direction = direction, start_text = text, shift_amount = shift)
#encrypt(text = text, shift = shift) 