alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(cipher_direction, start_text, shift_amount):
    end_text = ""
    for i in start_text:
        
        if direction == "encode":
            if i == " ":
                new_letter = "*"
                end_text += new_letter
            elif i == ".":
                new_letter = "~"
                end_text += new_letter
            elif i == ",":
                new_letter = "`"
                end_text += new_letter
            else: 
                position = alphabet.index(i)                
                new_position = position + shift
                new_letter = alphabet[new_position]
                end_text += new_letter
        elif direction == "decode":
            if i == "*":
                new_letter = " "
                end_text += new_letter 
            elif i == "~":
                new_letter = "."
                end_text += new_letter
            elif i == "`":
                new_letter = ","
                end_text += new_letter
            else:
                position = alphabet.index(i) 
                new_position = position - shift
                new_letter = alphabet[new_position]
                end_text += new_letter  

        
    print(f"the {cipher_direction}d message is : {end_text}")


    
cipher(cipher_direction = direction, start_text = text, shift_amount = shift)
#encrypt(text = text, shift = shift) 
