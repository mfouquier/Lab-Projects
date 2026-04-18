alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(encode_or_decode, original_text, shift_amount):
    returned_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            returned_text += char
        else:
            new_index = alphabet.index(char) + shift_amount 
            new_index %= len(alphabet)
            returned_text += alphabet[new_index]

    print(f"Here is your {encode_or_decode}d message {returned_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Would you like to continue 'yes' or 'no'?")

    if restart == 'no':
        should_continue = False
        print("Goodbye")


# def encrypt(original_text, shift):
#     encoded_text = ""

#     for char in original_text:
#         if char in alphabet:
#             index = alphabet.index(char)
#             new_index = (index + shift) % 26
#             encoded_text += alphabet[new_index]
#     print(encoded_text)


# def decrypt(encrypted_text, shift):
#     decoded_text = ""

#     for char in encrypted_text:
#         if char in alphabet:
#             index = alphabet.index(char)
#             new_index = index - shift % 26
#             decoded_text += alphabet[new_index]
#     print(decoded_text)

#decrypt(encrypted_text=text, shift=shift)
#encrypt(original_text=text, shift=shift)