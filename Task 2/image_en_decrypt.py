from PIL import Image
import random
import sys

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, output_path):
    image.save(output_path)

def encrypt_image(image, key):
    pixels = image.load()
    width, height = image.size
    random.seed(key)
    
    for y in range(height):
        for x in range(width):
            new_x = random.randint(0, width - 1)
            new_y = random.randint(0, height - 1)
            pixels[x, y], pixels[new_x, new_y] = pixels[new_x, new_y], pixels[x, y]
    
    return image

def decrypt_image(image, key):
    pixels = image.load()
    width, height = image.size
    random.seed(key)
    
    swaps = []
    for y in range(height):
        for x in range(width):
            new_x = random.randint(0, width - 1)
            new_y = random.randint(0, height - 1)
            swaps.append(((x, y), (new_x, new_y)))
    
    for (x, y), (new_x, new_y) in reversed(swaps):
        pixels[x, y], pixels[new_x, new_y] = pixels[new_x, new_y], pixels[x, y]
    
    return image

if __name__ == "__main__":
    operation = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    key = int(sys.argv[4])

    image = load_image(input_path)
    
    confirmation = int(input("Confirm your key?: \n"))
    if confirmation == key:
        if operation == "encrypt":
            encrypted_image = encrypt_image(image.copy(), key)
            save_image(encrypted_image, output_path)
            print(f"Image successfully encrypted and saved to {output_path}")
        elif operation == "decrypt":
            decrypted_image = decrypt_image(image.copy(), key)
            save_image(decrypted_image, output_path)

            print(f"Image successfully decrypted and saved to {output_path}")
        else:
            print("Invalid operation. Use 'encrypt' or 'decrypt'.")
    else:
        print("This image is not intended for you.")
