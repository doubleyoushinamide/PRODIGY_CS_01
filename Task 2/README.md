# Image Encryption Tool

This Python script provides a simple image encryption and decryption tool using pixel manipulation. The tool allows users to encrypt and decrypt images by swapping pixel values based on a provided key.

## Features

- **Encrypt Images**: Randomly swaps pixel values to encrypt the image.
- **Decrypt Images**: Reverses the pixel swaps to restore the original image.
- **Key Confirmation**: Ensures that only users with the correct key can encrypt or decrypt the image.

## Prerequisites

- Python 3.x
- Pillow library

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Install the Pillow library using pip:

   ```bash
   pip install pillow
   ```

## Usage

### Encrypt an Image

To encrypt an image, use the following command:

```bash
python3 image_encryption.py encrypt <input_image_path> <output_image_path> <key>
```

Example:

```bash
python3 image_encryption.py encrypt path/to/your/image.jpg path/to/save/encrypted_image.jpg 42
```

### Decrypt an Image

To decrypt an image, use the following command:

```bash
python3 image_encryption.py decrypt <input_image_path> <output_image_path> <key>
```

Example:

```bash
python3 image_encryption.py decrypt path/to/save/encrypted_image.jpg path/to/save/decrypted_image.jpg 42
```

### Key Confirmation

When you run the script, you will be prompted to confirm your key. If the entered key does not match the provided key, the script will print a message indicating that the image is not intended for you.

## Script Overview

```python
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
            key_dec = int(input("Enter your key: \n"))
            if key_dec == key:
                decrypted_image = decrypt_image(image.copy(), key_dec)
                save_image(decrypted_image, output_path)
                print(f"Image successfully decrypted and saved to {output_path}")
            else:
                print("Wrong key! \n Contact Admin!")
        else:
            print("Invalid operation. Use 'encrypt' or 'decrypt'.")
    else:
        print("This image is not intended for you.")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive overview of how to use the image encryption tool, along with example commands and a brief explanation of the script's functionality.
