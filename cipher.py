def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            encrypted_text += new_char
        else:
            encrypted_text += char
    
    return encrypted_text

# Ask user for a sentence
plain_text = input("Please enter a sentence: ")

# Encrypt the text with a shift of 5
encrypted_text = caesar_cipher(plain_text, 5)

# Print the encrypted sentence
print("The encrypted sentence is:", encrypted_text)
