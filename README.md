# FUTURE_CS_03
# Secure File Portal with AES Encryption

## Overview
A web portal built with **Python Flask** to securely **upload, download, and delete files**.  
All files are encrypted using **AES** before being stored and decrypted automatically on download, ensuring data security.

---

## Features
- Secure file upload with AES encryption  
- Download files with automatic decryption  
- Secure deletion of files  
- User-friendly interface  

---

## Project Structure

SecureFilePortal/
│
├── app.py # Main Flask app
├── crypto_utils.py # AES encryption/decryption functions
├── templates/
│ └── index.html # Web interface

├── uploads/ # Encrypted files storage
└── README.md # Project documentation

---

Usage
Upload Files – Select a file and click Upload & Encrypt.

Download Files – Click Download to get a decrypted copy.

Delete Files – Click Delete to securely remove a file.

Security Overview
AES encryption ensures files are safe at rest

Files are encrypted before saving; plaintext never stored

Deletion is via POST request with confirmation

Dependencies
Python 3.x

Flask

python-dotenv

cryptography

Author
Mayur Jadhav – B.Voc Cybersecurity Student
Email: mjmayurjadhav2@gmail.com
