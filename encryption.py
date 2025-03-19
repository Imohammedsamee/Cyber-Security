from PIL import Image
import stepic

# Get user input
message = input("Enter secret message: ")
passcode = input("Enter a passcode: ")

# Convert message to bytes
message_bytes = (passcode + message).encode()

# Open an image (Use your own image path)
img = Image.open("inputImage.png")  # Ensure this image exists

# Encode message in image
encoded_img = stepic.encode(img, message_bytes)

# Save encrypted image
encoded_img.save("encryptedImage.png")
print("Message encrypted and saved as encryptedImage.png")
