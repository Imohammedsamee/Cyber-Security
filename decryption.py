from PIL import Image
import stepic

# Get passcode from user
entered_passcode = input("Enter passcode for decryption: ")

# Open encrypted image
encoded_img = Image.open("encryptedImage.png")

# Decode message
decoded_bytes = stepic.decode(encoded_img)
decoded_message = decoded_bytes.decode()

# Verify passcode
if decoded_message.startswith(entered_passcode):
    print("Decrypted message:", decoded_message[len(entered_passcode):])
else:
    print("Incorrect passcode! Decryption failed.")
