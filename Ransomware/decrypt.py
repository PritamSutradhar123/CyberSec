from cryptography.fernet import Fernet
import os

# load key
with open("thekey.key", "rb") as kf:
    key = kf.read()
    print(key)
f = Fernet(key)

files = []
for fname in os.listdir():
    if os.path.isfile(fname):
        # skip known files (your script, key, decrypt script)
        if fname in {"encrypt.py", "thekey.key", "decrypt.py"}:
            continue
        files.append(fname)

print("Will try to decrypt:", files)

for path in files:
    
    # open in read+write binary once
    with open(path, "rb") as fh:
        data = fh.read()  
    decrypted_data = f.decrypt(data)
    with open(path, "wb") as a:    
        
        a.write(decrypted_data)

    
print("Done — attempted decryption on listed files.")

# If you really want to delete this script after successful run, uncomment:
os.remove(__file__)
