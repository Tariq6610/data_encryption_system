from auth import Users
from data import DataEncription
import streamlit as st
from app_pages.home import home_page
from app_pages.login import login_page
from app_pages.sigup import signUp_page
from app_pages.utils.logout import logout
from cryptography.fernet import Fernet
from key_manager import load_or_create_key
import hashlib
import os

KEY = load_or_create_key()
cipher = Fernet(KEY)

# if not os.path.exists("secret.key"):
#     with open("secret.key", "wb") as f:
#         f.write(Fernet.generate_key())

# if os.path.exists("secret.key"):
#     try:
#         with open("secret.key", "rb") as f:
#             KEY = f.read()
#             print(KEY)
#             # Attempt to initialize Fernet with the key to validate it
#             cipher = Fernet(KEY)
#     except Exception as e:
#         print(f"❌ Error loading key: {e}")
#         exit(1)
    



    

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function To encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()






def store_data(user,encrypted_text, hashed_passkey):
    user_data = DataEncription(user, hashed_passkey, encrypted_text)
    user_data.add_data()

def retrieve_data(name, key):
    # possible_errors = ["No data Found", "Invalid passkey", "No user found"]
    chances = 3
    while chances:
        data =  DataEncription.retreive_data(name, key)
        if data != "Invalid passkey":
            return data
        elif data == "Invalid passkey":
            chances -= 1
            return None
        

# Function to decrypt data
def decrypt_data(user, passkey):
    hashed_passkey = hash_passkey(passkey)
    recived_data = retrieve_data(user, hashed_passkey)

    if recived_data:
        decrypt =  cipher.decrypt(recived_data.encode()).decode()
        print(decrypt)
        return decrypt
    else:
        return None
    
    # failed_attempts += 1





def dashboard():
    user = st.query_params.get("user")
    st.sidebar.markdown(f"""**{user}**
                        
---                  
                        """)
    # Navigation
    menu = ["Home", "Store Data", "Retrieve Data"]
    choice = st.sidebar.radio("Navigation", menu)
    st.sidebar.markdown("---")
    if choice == "Home":
        home_page()
    elif choice == "Store Data":
        st.subheader("📂 Store Data Securely")
        user_data = st.text_area("Enter Data:")
        passkey = st.text_input("Enter Passkey:", type="password", key="add_passkey")

        if st.button("Encrypt & Save"):
            if user_data and passkey:
                hashed_passkey = hash_passkey(passkey)
                encrypted_text = encrypt_data(user_data)
                store_data(user,encrypted_text, hashed_passkey)
                st.success("✅ Data stored securely!")
            else:
                st.error("⚠️ Both fields are required!")

    elif choice == "Retrieve Data":
        st.subheader("🔍 Retrieve Your Data")
        passkey = st.text_input("Enter Passkey:", type="password", key="retreive_passkey")

        if "failed_attempts" not in st.session_state:
            st.session_state.failed_attempts = 0

        if st.button("Decrypt"):
            if  passkey:
                decrypted_text = decrypt_data(user, passkey)

                if decrypted_text:
                    st.success(f"✅ Decrypted successfull :")
                    st.info(decrypted_text)
                else:
                    st.session_state.failed_attempts += 1
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")
                    # st.rerun()


                    if st.session_state.failed_attempts >= 3:
                        st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                        st.query_params["page"] = "signIn"
                        st.session_state.failed_attempts = 0
                        st.rerun()
            else:
                st.error("⚠️ Both fields are required!")


    if st.sidebar.button("log Out"):
        logout()

    st.sidebar.markdown("---")

    st.sidebar.markdown("""
<div style="display: flex; gap: 10px; justify-content: end;">
    <a href="https://github.com/Tariq6610" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/24/733/733553.png" alt="GitHub">
    </a>
    <a href="https://linkedin.com/in/tariq-syed-788940289" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/24/174/174857.png" alt="LinkedIn">
    </a>
    <a href="https://www.facebook.com/share/12J6Bn1WZ6R/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/24/733/733547.png" alt="Facebook">
    </a>
</div>
""", unsafe_allow_html=True)
    

    
        




def main():
    if "page" not in st.query_params:
        st.query_params.update(page = "signIn")
    page = st.query_params.get("page", "signIn")

    if page == "signIn":
        login_page()
    elif page == "signUp":
        signUp_page()
    elif page == "home":
        dashboard()

        

    

    


    
    


    

    



if __name__ == "__main__":
    main()
