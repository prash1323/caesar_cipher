alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(original_text, shift_amount):
    cipher = ""
    for letters in original_text:
        shifted_position = alphabet.index(letters) - shift_amount
        shifted_position = shifted_position % len(alphabet)
        cipher = cipher + alphabet[shifted_position]

    print(f"The decrypted result is: {cipher}")

def encrypt(original_text,shift_amount):
    cipher= ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        cipher = cipher + alphabet[shifted_position]

    print(f"The encrypted result is: {cipher}")

def caesar(original_text, shift_amount, encode_or_decode):
    final_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
          shift_amount = shift_amount * -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        final_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {final_text}")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
