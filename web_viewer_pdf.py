import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# 路徑
PDF_DIR = r"Nicktest\Python-PDF-Encoding-Toolkit\TXT_to_PDF"
PDF_FILENAME = "Nicktest_to_TXT_PDF_demo.pdf"

# 撰寫簡易HTML，透過頁面開啟PDF
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Nicktest PDF 預覽器</title>
    <style>
        body { font-family: "Microsoft JhengHei", sans-serif; text-align: center; padding: 50px; }
        .btn { padding: 15px 30px; font-size: 18px; cursor: pointer; background: #007bff; color: white; border: none; border-radius: 5px; }
        .btn:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>線上開啟PDF檔案</h1>
    <p>點擊下方按鈕，直接在瀏覽器開啟產出的 PDF 檔案</p>
    <br>
    <a href="/view-pdf" target="_blank">
        <button class="btn">立即開啟 PDF</button>
    </a>
</body>
</html>
"""

@app.route('/')
def index():
    """首頁：顯示預覽按鈕"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/view-pdf')
def view_pdf():
    """傳送 PDF 檔案"""
    # 使用 send_from_directory 確保檔案能安全地從目錄送出
    # as_attachment=False 在瀏覽器開啟，而不是直接下載
    return send_from_directory(
        directory=PDF_DIR, 
        path=PDF_FILENAME, 
        as_attachment=False
    )

if __name__ == "__main__":
    # 啟動 Flask 伺服器
    print("🚀 Nicktest PDF預覽伺服器啟動中")
    print(f"本機端測試")
    app.run(debug=True)
