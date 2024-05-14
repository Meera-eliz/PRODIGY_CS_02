from PIL import Image

def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        print("Error: Input image file not found.")
        exit()

def encrypt_image(image, key):
    encrypted_pixels = []
    for pixel in image.getdata():
        encrypted_pixel = tuple(pix ^ key for pix in pixel)  # XOR operation with key
        encrypted_pixels.append(encrypted_pixel)
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_pixels = []
    for pixel in encrypted_image.getdata():
        decrypted_pixel = tuple(pix ^ key for pix in pixel)  # XOR operation with key
        decrypted_pixels.append(decrypted_pixel)
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(decrypted_pixels)
    return decrypted_image

def save_image(image, output_path):
    image.save(output_path)

def main():
    image_path = "input_image.jpg"  # Corrected file name or path
    key = 123  # Example key, you can choose any integer
    image = load_image(image_path)
    
    encrypted_image = encrypt_image(image, key)
    save_image(encrypted_image, "encrypted_image.jpg")
    
    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, "decrypted_image.jpg")

if __name__ == "__main__":
    main()
