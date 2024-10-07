def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            decrypted_text += char
    return decrypted_text


def main():
    print("Caesar Cipher Program")
    choice = input("Choose an option: \n1. Encrypt a message \n2. Decrypt a message\n")
    
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    
    else:
        print("Invalid choice. Please select option 1 or 2.")


if __name__ == "__main__":
    main()
