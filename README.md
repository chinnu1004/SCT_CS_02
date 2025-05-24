# 🛡️ Image Encryption Tool (Flask + HTML)

A simple web-based image encryption tool that inverts the colors of an uploaded image using Python (Flask) on the backend and HTML + JavaScript on the frontend.

---

## 🚀 Features

- Upload any image (PNG, JPG, etc.)
- Simple encryption using RGB color inversion
- View the encrypted image in your browser

---

## 📁 Project Structure

```
image_encryptor/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend interface
```

---

## 🛠 Requirements

- Python 3.7+
- Flask
- Pillow (PIL)

Install the dependencies:

```bash
pip install flask pillow
```

---

## ▶️ How to Run the App

1. Clone the repo or extract the project ZIP
2. Open a terminal in the project directory
3. Run the Flask server:

```bash
python app.py
```

4. Open your browser and go to:

```
http://127.0.0.1:5000
```

5. Upload an image and click "Encrypt" to see the result.

---

## 🧠 How It Works

- The frontend uses a form to upload an image.
- The backend receives the image, inverts its RGB colors, and sends it back as a new image.
- The browser displays the encrypted image.

---

## 🧩 Example Encryption

Original → Encrypted  
🎨 (Color) → 🔄 (Inverted Color)

---

## 📌 Future Ideas

- Add decryption support
- Use advanced encryption (e.g., AES + pixel scramble)
- Add a "Download Encrypted Image" button
- Store encrypted files on the server

---

## 📄 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Author

Developed with ❤️ using Python & Flask.
