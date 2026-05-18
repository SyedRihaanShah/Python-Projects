import Crypto_utils as cu
import streamlit as st 
import json
import os

FILE_NAME = 'passwords.json'
st.title("PASSWORD ENCRYPTER", text_alignment="center")

website_name = st.text_input(label="Website Name" ,placeholder="Enter here")
user_name = st.text_input(label="User Name", placeholder="Enter here")
password = st.text_input(label='Password', placeholder="Enter password",type="password")

if st.button(label="Submit"): 
    encrypted_pass = cu.encryption(password)
    st.success("Password saved")

    st.write("Website: ", website_name)
    st.write("Username: ", user_name)
    st.write("Encypted_password: ", encrypted_pass)

    data_new = {
        "website" : website_name,
        "username" : user_name,
        "password" : encrypted_pass
    }
    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
    
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
        
    data.append(data_new)

    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

with open("passwords.json", "rb") as file:
    st.download_button(
        label="Download Password File",
        data=file,
        file_name="passwords.json",
        mime='applications/json'
    )

st.header("PASSWORD DECRYPTER", text_alignment='center')

encrypted_password = st.text_input(
    label= 'Enter encrpyted password',
    placeholder=  'Enter here'
)
if st.button("Decrpyt"):
    try:
        decrpted_password = cu.decryption(encrypted_password)
        st.success("Password Decrypted")
        st.text_input(
            label="Dectypted password",
            value=decrpted_password,
            type='password'
        )
    
    except:
        st.error("Invalid encryted password/ key doesnt exist anymore")