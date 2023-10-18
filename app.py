from flask import Flask, render_template, request
from text_analyzer import analyze_text
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 업로드할 파일을 저장할 폴더 경로

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        # 파일 업로드 처리
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                with open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), 'r', encoding='cp949') as uploaded_file:
                    text = uploaded_file.read()
                    result = analyze_text(text, file.filename)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)