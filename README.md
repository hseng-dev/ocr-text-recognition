# OCR文字识别应用

这是一个基于Flask和Tesseract的OCR文字识别Web应用，可以从图片中提取文字。

## 功能特点

- 支持拖放上传图片
- 支持多种图片格式（PNG, JPG, JPEG, GIF）
- 实时显示上传和处理进度
- 支持中英文识别
- 可一键复制识别结果

## 安装要求

1. Python 3.7+
2. Tesseract-OCR
3. 中文语言包

## 安装步骤

1. 安装Tesseract-OCR：
   - Windows: 下载并安装 [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - 确保将Tesseract添加到系统环境变量中

2. 安装Python依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```bash
   python app.py
   ```

4. 在浏览器中访问：
   ```
   http://localhost:5000
   ```

## 使用说明

1. 打开网页后，可以通过点击上传区域选择图片，或直接将图片拖放到上传区域
2. 上传完成后，系统会自动进行文字识别
3. 识别结果会显示在右侧文本框中
4. 点击"复制文本"按钮可以复制识别结果

## 注意事项

- 请确保图片清晰度较高，以获得更好的识别效果
- 支持的最大文件大小为16MB
- 建议使用黑色文字白色背景的图片以获得最佳效果 