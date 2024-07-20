# Caesar Cipher Message Encryption Program

## Overview

This Python script implements the Caesar Cipher algorithm for encrypting and decrypting user messages. It allows a user to input a message, encrypt it using a Caesar Cipher with a shift value of 3, and then provides the recipient with the option to read or discard the message.

## Features

- **User Input Validation**: Ensures that the input message does not contain numbers and does not exceed 18 words.
- **Encryption**: Uses the Caesar Cipher algorithm with a shift value of 3 to encrypt the message.
- **Decryption**: Decrypts the message when the recipient chooses to read it.
- **Error Handling**: Handles invalid inputs gracefully with appropriate error messages.

## Functionality

### Encrypting a Message

1. **User Input**: The sender is prompted to input their message to the recipient.
   - The message must be a string containing only alphabetic characters and spaces.
   - The length of the message must not exceed 18 words.
2. **Encryption Process**: The message is encrypted using the Caesar Cipher algorithm with a shift value of 3.
3. **Display Encrypted Message**: The encrypted message is displayed to the sender.

### Decrypting a Message

1. **Recipient Prompt**: The recipient is prompted with the message: "You have an unread message. Press 1 to read and 2 to discard."
   - If the recipient presses `1`, the message is decrypted and displayed.
   - If the recipient presses `2`, the program terminates with the message "You have no unread messages."

## Usage

1. **Run the Script**: Execute the script using Python.
2. **Input the Message**: When prompted, enter the message to be encrypted.
   - Ensure the message does not contain numbers and does not exceed 18 words.
3. **View Encrypted Message**: The encrypted message will be displayed.
4. **Recipient Interaction**: The recipient will be prompted to read or discard the message.
   - Press `1` to read the decrypted message.
   - Press `2` to discard the message and terminate the program.

## Code Explanation

```python
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift if char.islower() else shift
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)

def display_encrypted_message(encrypted_message):
    print(f"Encrypted Message: {encrypted_message}")

def main():
    try:
        message = input("Enter your message to the recipient (max 18 words): ")
        if not all(char.isalpha() or char.isspace() for char in message):
            print("Kindly input words that do not contain numbers")
            return
        
        words = message.split()
        if len(words) > 18:
            print("Message exceeds the 18-word limit.")
            return
        
        shift = 3
        encrypted_message = encrypt_message(message, shift)
        display_encrypted_message(encrypted_message)
        
        action = input("You have an unread message. Press 1 to read and 2 to discard: ")
        if action == '1':
            decrypted_message = decrypt_message(encrypted_message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif action == '2':
            print("You have no unread messages.")
        else:
            print("Invalid input.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Functions

- `encrypt_message(message, shift)`: Encrypts the input message using the Caesar Cipher algorithm with the specified shift value.
- `decrypt_message(encrypted_message, shift)`: Decrypts the encrypted message using the negative shift value.
- `display_encrypted_message(encrypted_message)`: Displays the encrypted message.
- `main()`: Main function that handles user input, message validation, encryption, and decryption.

### Error Handling

- Ensures the input message does not contain numbers.
- Ensures the input message does not exceed 18 words.
- Handles invalid inputs gracefully and provides appropriate error messages.

## Requirements

- Python 3.x

## Running the Script

1. Save the script to a file, e.g., `caesar_cipher.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using Python:

```sh
python caesar_cipher.py
```

Follow the prompts to input your message and interact with the program as the recipient.
