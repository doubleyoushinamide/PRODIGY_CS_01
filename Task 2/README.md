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

---
