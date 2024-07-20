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
        message = input("Enter your message to the recipient (max 18 words): \n")
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
        
        action = input("You have an unread message. Press 1 to read and 2 to discard: \n")
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
