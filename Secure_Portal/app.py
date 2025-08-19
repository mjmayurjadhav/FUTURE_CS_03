# app.py
import os
from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename

from crypto_utils import load_key, encrypt_data, decrypt_data

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

key = load_key()  # Load encryption key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename != "":
            filename = secure_filename(file.filename)
            data = file.read()
            encrypted_data = encrypt_data(data, key)
            # Save encrypted file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename + ".enc"), 'wb') as f:
                f.write(encrypted_data)
            return redirect('/')
    # List encrypted files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    # Encrypted file path
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_data(encrypted_data, key)

    # Save decrypted temporarily
    temp_path = os.path.join("decrypted_" + filename.replace(".enc", ""))
    with open(temp_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(temp_path, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted file: {filename}")  # optional: server log
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=5003)





