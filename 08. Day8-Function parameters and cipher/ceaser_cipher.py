'''
Ceaser Cipher
This is a simple implementation of the Ceaser Cipher algorithm.
The Ceaser Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of
places down or up the alphabet. 
For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method wraps around the alphabet
so that Z becomes A.
The cipher can be used to encrypt and decrypt messages.
The function takes a string and an integer as input. The string is the message to be encrypted or decrypted, and the integer
is the shift value. A positive shift value will encrypt the message, while a negative shift value will decrypt it.
The function returns the encrypted or decrypted message.
The function is case-insensitive and ignores non-alphabetic characters.
'''

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

## create a function called encrypt that takes a string and an integer as input and shifts the letters in the string by the integer
def encrypt(text,shift):
    encrypted_text=""
    for letter in text:
        index=alphabet.index(letter)
        new_index=(index+shift)%26
        encrypted_text+=alphabet[new_index]
    return encrypted_text

## create a function called decrypt that takes a string and an integer as input and shifts the letters in the string by the integer

def decrypt(encrypted_text,shift):
    decrypted_text=""
    for letter in encrypted_text:
        index=alphabet.index(letter)
        new_index=(index-shift)%26
        decrypted_text+=alphabet[new_index]
    return decrypted_text

## single function for both encryption and decryption
def ceaser_cipher(text,shift,direction):
    if direction=="encode":
        encrypted= encrypt(text,shift)
        print(f"The encrypted text is: {encrypted}")
    elif direction=="decode":
        decrypted= encrypt(text,-shift)
        print(f"The decrypted text is: {decrypted}")
    else:
        return "Invalid direction"
    
## call the function
ceaser_cipher(text,shift,direction)