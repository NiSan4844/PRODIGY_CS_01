# Caesar Cipher Text Encryption and Decryption

## Overview
This project implements a simple Caesar Cipher algorithm in Python for encrypting and decrypting text messages. The Caesar Cipher is a basic encryption technique that shifts characters in the alphabet by a specified number of positions.

## Features
- Encrypts plain text messages using a user-defined shift value.
- Decrypts previously encrypted messages using the same shift value.
- Handles both uppercase and lowercase letters while leaving non-alphabetic characters unchanged.

## Table of Contents

- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Future Improvements](#future-improvements)
- [License](#license)

## Usage
To use the Caesar Cipher program, run the following command in your terminal:
```bash
python caesar_cipher.py
```
You will be prompted to choose between encrypting or decrypting a message. Follow the on-screen instructions to input your message and shift value.

1. **Encrypt a Message**: Choose option 1, enter your message, and specify the shift value. The program will output the encrypted message.
2. **Decrypt a Message**: Choose option 2, enter the encrypted message, and specify the same shift value. The program will output the original message.

## Code Explanation
The main components of the program include:

1. **Encryption Function**: 
   - `caesar_cipher_encrypt(plain_text, shift)`: Shifts each character in `plain_text` by the specified `shift`, wrapping around the alphabet as necessary.

2. **Decryption Function**: 
   - `caesar_cipher_decrypt(cipher_text, shift)`: Shifts each character in `cipher_text` back by the specified `shift` to retrieve the original message.

3. **User Interaction**:
   - The `main()` function handles user input and invokes the appropriate functions for encryption or decryption.

4. **Execution Control**: 
   - The `if __name__ == "__main__":` block ensures that the program runs only when executed directly.

## Future Improvements
Here are some ideas for enhancing the project in the future:
- **User Interface**: Develop a graphical user interface (GUI) to improve user experience.
- **Input Validation**: Add error handling for invalid inputs (e.g., non-integer shift values).
- **Custom Alphabet**: Allow users to define a custom alphabet for encryption and decryption.
- **Brute Force Decryption**: Implement a method to automatically decrypt messages without knowing the shift value.
- **Support for Unicode Characters**: Extend functionality to support encryption and decryption of Unicode characters beyond the basic alphabet.