# Password Manager

A simple password manager built using Streamlit and Python.

This application allows users to:
- Encrypt passwords securely using Fernet encryption
- Store encrypted passwords in a JSON file
- Decrypt encrypted passwords
- Download stored password data

---

## Features

- Password encryption and decryption
- Secure key generation using Fernet
- JSON-based password storage
- Download password database
- Simple and clean Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- Cryptography (Fernet)
- JSON

---

## Project Structure

```text
Password_Manager/
│
├── app.py
├── Crypto_utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPO_LINK
```

Move into the project folder:

```bash
cd Password_Manager
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

---

## Security Notes

- `key.key` is excluded using `.gitignore`
- Passwords are stored in encrypted format
- Never upload encryption keys publicly

---

## Author

Syed_Rihaan_Shah