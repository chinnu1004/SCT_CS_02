from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files:
        return 'No image uploaded!', 400

    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')

    # Invert RGB colors for simple encryption
    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
