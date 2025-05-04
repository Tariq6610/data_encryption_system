import os
import sys
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def load_or_create_key(create_if_missing = False):
    if os.path.exists("secret.key"):
        try:
            with open("secret.key", "rb") as f:
                KEY = f.read()
                Fernet(KEY)
                return KEY
        except Exception as e:
            print(f"❌ Error loading key: {e}")
            sys.exit(1)
    else:
        if create_if_missing:
            key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as f:
                f.write(key)
            print("✅ Key generated.")
            return key
        else:
            print("❌ Key file not found. Use python generate_key.py to create one.")
            sys.exit(1)
    