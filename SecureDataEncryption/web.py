import streamlit as st
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64, os

st.title("Secure Data Encryption and Decryption")

menu = ["Home", "Encryption", "Decryption", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

def generate_fernet_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def generate_salt():
    return os.urandom(16)

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

def home():
    st.subheader("Home")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    st.info("Go to the Login page to authenticate.")

def Encryption():
    st.subheader("Encryption")
    encryption_data = st.text_input("Enter data to encrypt")
    master_key = st.text_input("Enter Master Key", type="password")

    if st.session_state.failed_attempts >= 3:
        st.error("Too many failed attempts. Please try again later.")
        st.info("Go to the Login page to re-authenticate.")
        return

    if st.button("Encrypt", key="encrypt_button"):
        if "salt" not in st.session_state or "key" not in st.session_state:
            st.warning("Please login first to generate encryption key.")
            return

        salt = st.session_state.salt
        key = st.session_state.key

        if key == generate_fernet_key_from_password(master_key, salt):
            encrypted_data = encrypt_data(encryption_data, key)
            st.text_area("Encrypted data (copy this for decryption):", encrypted_data.decode(), height=150)
            st.success("Data encrypted successfully")
        else:
            st.session_state.failed_attempts += 1
            st.error("Incorrect key")
            st.write("Attempts left: {}".format(3 - st.session_state.failed_attempts))

def Decryption():
    st.subheader("Decryption")
    encrypted_input = st.text_area("Enter encrypted data to decrypt (paste exact string)", height=150)
    master_key = st.text_input("Enter Master Key", type="password")

    if st.session_state.failed_attempts >= 3:
        st.error("Too many failed attempts. Please try again later.")
        st.info("Go to the Login page to re-authenticate.")
        return

    if st.button("Decrypt"):
        if "salt" not in st.session_state or "key" not in st.session_state:
            st.warning("Please login first to generate decryption key.")
            return

        salt = st.session_state.salt
        expected_key = st.session_state.key
        entered_key = generate_fernet_key_from_password(master_key, salt)

        if entered_key == expected_key:
            try:
                decrypted_data = decrypt_data(encrypted_input.encode(), entered_key)
                st.success("Decrypted data: " + decrypted_data)
            except Exception:
                st.error("Decryption failed. Invalid data or wrong key.")
        else:
            st.session_state.failed_attempts += 1
            st.error("Incorrect Master Key")
            st.write("Attempts left: {}".format(3 - st.session_state.failed_attempts))

def Login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.salt = generate_salt()
        st.session_state.key = generate_fernet_key_from_password(password, st.session_state.salt)
        st.session_state.failed_attempts = 0
        st.success("Logged in as {}".format(username))

if choice == "Home":
    home()
elif choice == "Encryption":
    Encryption()
elif choice == "Decryption":
    Decryption()
elif choice == "Login":
    Login()
