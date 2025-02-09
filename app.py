from flask import Flask, request, jsonify, render_template
import os
import sys
from PIL import Image
import pytesseract
from werkzeug.utils import secure_filename
import traceback

def resource_path(relative_path):
    """ 获取资源绝对路径 """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 设置Tesseract-OCR路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.expanduser('~'), 'OCR_uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有文件上传'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # 检查文件是否存在
            if not os.path.exists(filepath):
                return jsonify({'error': '文件保存失败'}), 500

            # 检查Tesseract路径
            if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
                return jsonify({'error': f'Tesseract未找到，请确认安装路径：{pytesseract.pytesseract.tesseract_cmd}'}), 500

            # 使用pytesseract进行OCR识别
            image = Image.open(filepath)
            try:
                text = pytesseract.image_to_string(image, lang='chi_sim+eng')
            except Exception as e:
                print(f"OCR错误: {str(e)}")
                print(f"错误详情: {traceback.format_exc()}")
                return jsonify({'error': f'OCR识别失败: {str(e)}'}), 500
            
            # 删除临时文件
            os.remove(filepath)
            
            return jsonify({'text': text})
        except Exception as e:
            print(f"处理错误: {str(e)}")
            print(f"错误详情: {traceback.format_exc()}")
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': f'处理失败: {str(e)}'}), 500
    
    return jsonify({'error': '不支持的文件类型'}), 400

if __name__ == '__main__':
    app.run(debug=True) 