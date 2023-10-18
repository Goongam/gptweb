from textblob import TextBlob
import os
from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 업로드할 파일을 저장할 폴더 경로

def analyze_text(text, name):
    with open(os.path.join(app.config['UPLOAD_FOLDER'], name), 'r', encoding='cp949') as uploaded_file:
        text = uploaded_file.read()
        analysis = TextBlob(text)
        sentiment = analysis.sentiment
        return sentiment