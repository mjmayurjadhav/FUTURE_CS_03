# FUTURE_CS_03
# Secure File Portal – Walkthrough

This document explains how to use the **Secure File Portal** to upload, download, and delete files securely with AES encryption.

---

## 1. Project Setup

##1. Clone the repository:

git clone https://github.com/mjmayurjadhav/FUTURE_CS_03.git 

cd SecureFilePortal

Install dependencies:

pip install flask python-dotenv cryptography

Create a demo.txt file in the project root:

Hello 

Myself Mayur Jadhav 

From B.K.Birla Collge 

Cyber Security Intern at FutureInterns

Run the Flask app:

python app.py

Open in your browser: http://127.0.0.1:5003/

2. Uploading Files

On the portal homepage, click Choose File.

Select a file from your computer.

Click Upload & Encrypt.

The file will be encrypted and appear in the Encrypted Files list with .enc extension.

3. Downloading Files

Click Download next to the file you want.

The file will be decrypted automatically and downloaded to your computer.

You can verify that the downloaded file matches the original content.

4. Deleting Files

Click Delete next to the file you want to remove.

A confirmation prompt will appear. Click OK to delete.

The encrypted file is permanently removed from the server.

5. Security Highlights
   
AES Encryption: All files are encrypted at rest.

Key Management: AES key is stored in .env, never in code.

Secure File Handling: Plaintext files are never stored on the server.

Safe Deletion: Files are removed via POST requests with user confirmation.

Optional: file integrity checks (e.g., SHA256) can be added.

6. Summary
   
This walkthrough demonstrates how to securely manage files in the portal using AES encryption, ensuring confidentiality, integrity, and controlled access.

#Author 

Mayur Jadhav 
