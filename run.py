import os
import sys
import webbrowser
from threading import Timer
from app import app

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

def resource_path(relative_path):
    """ 获取资源绝对路径 """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # 确保模板目录存在
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # 确保上传目录存在
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # 设置延时打开浏览器
    Timer(1.5, open_browser).start()
    
    # 启动Flask应用
    app.run(port=5000) 