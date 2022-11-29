from cipher_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(cipher_direction, start_text, shift_amount):
    end_text = ""
    
    while shift_amount > int(len(alphabet)/2):
        m = shift_amount - int(len(alphabet)/2)
        shift_amount = m
    if cipher_direction == "encode":
        shift_amount *= -1
    for i in start_text:
        if i not in alphabet:
            end_text += i
        else: 
            position = alphabet.index(i) 
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"Here's the {cipher_direction}d message : {end_text}")
            
        
            
    
            


cipher(cipher_direction = direction, start_text = text, shift_amount = shift)
reply = input("Type 'yes' if you want to go again, otherwise type 'no':  ").lower()
while reply == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(cipher_direction = direction, start_text = text, shift_amount = shift)
    reply = input("Type 'yes' if you want to go again, otherwise type 'no':  ").lower()
print("Thank you goodbye")