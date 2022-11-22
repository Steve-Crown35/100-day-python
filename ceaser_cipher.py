import string
alphabet = list(string.ascii_lowercase)
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_message = ""
    for i in text: 
        if i == " " :
            encrypted_message += i  
        else: 
            i_to_ordinal= ord(i) + shift
            matched_alphabet = chr(i_to_ordinal)
            encrypted_message += matched_alphabet
    print(f"the encoded message is {encrypted_message}")

encrypt(text = text, shift = shift) 