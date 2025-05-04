import streamlit as st

def home_page():
        st.image("resources/images/banner.jpg", use_container_width=True)
        st.markdown("""
# 🔐 Secure Data Encryption App

Welcome to your personal **data vault**, built with **Python** and **Streamlit**!

---

### 💾 In-Memory Data Storage
- Data is securely stored with hashed passkeys.

---

### 🔒 Encryption & Decryption
- Choose between:
  - **Caesar Cipher** (simple substitution)
  - **Fernet** (secure AES-based encryption via `cryptography`)
- Decryption requires the **correct passkey**.

---

### 🛡️ Authentication & Security
- Users get **3 passkey attempts** before being redirected to a **Login Page**.
- Failed attempts are **counted and displayed**.

---

### 🧠 Streamlit Interface
- **🏠 Home Page**: Choose to store or retrieve data.
- **➕ Insert Data Page**: Enter your text + passkey to encrypt and save it.
- **🔓 Retrieve Data Page**: Provide the correct passkey to decrypt your data.
- **🔐 Login Page**: Reauthorize access after 3 failed attempts.

---

Enjoy secure and simple encryption — all inside your browser!
""")
