import os
from fpdf import FPDF

# 路徑
source_file = r"Nicktest\Python-PDF-Encoding-Toolkit\Big5_to_utf8\big5_utf8.txt"
output_dir = r"Nicktest\Python-PDF-Encoding-Toolkit\TXT_to_PDF"
output_file = os.path.join(output_dir, "Nicktest_to_TXT_PDF_demo.pdf")

# 檢查資料夾，沒有的話自動補一個
os.makedirs(output_dir, exist_ok=True)

def generate_demo_pdf():
    pdf = FPDF()
    pdf.add_page()
    font_path = r"Nicktest.ttc" 

    try:
        # 使用num=0 指定 ttc 裡面第一個字體
        pdf.add_font("MSJH", style="", fname=font_path, num=0)

    except:
        # 萬一不支援num，嘗試最基本載入
        pdf.add_font("MSJH", style="", fname=font_path)

    #標題寫入,置中顯示
    pdf.set_font("MSJH", size=30) 
    pdf.cell(0, 15, "TXT轉PDF to Demo", ln=True, align='C')
    pdf.ln(5)

    try:
        #內文字體大小
        pdf.set_font("MSJH", size=12) 

        #讀取UTF-8,設計自動換行防跑版
        with open(source_file, "r", encoding="utf-8") as f:
            content = f.read()
            pdf.multi_cell(w=0, h=10, txt=content)
        
        pdf.output(output_file)
        print(f"✨ PDF 已生成：{output_file}")

    except Exception as e:
        print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    generate_demo_pdf()