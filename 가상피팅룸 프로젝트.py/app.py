from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# 옷 이미지들이 저장된 폴더
CLOTHES_FOLDER = os.path.join(app.static_folder, 'clothes')

# 이미지 리스트 JSON으로 반환
@app.route('/clothes')
def list_clothes():
    files = [f for f in os.listdir(CLOTHES_FOLDER) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    return jsonify(files)

# 개별 옷 이미지 제공
@app.route('/clothes/<filename>')
def get_cloth_image(filename):
    return send_from_directory(CLOTHES_FOLDER, filename)

# index.html 제공 (정적 HTML)
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
