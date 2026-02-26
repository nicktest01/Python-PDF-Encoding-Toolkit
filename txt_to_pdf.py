import os
from fpdf import FPDF

# 1. 設定路徑與檔名
base_path = r"C:\Users\Nicktest\Documents\nicktest_txt_to_pdf"
input_file = os.path.join(base_path, "utf8.txt")
output_file = os.path.join(base_path, "output.pdf")

# Windows 系統字體路徑 (直接抓系統的，不用手動複製檔案)
font_path = r"C:\Windows\Fonts\msjh.ttc" 

def convert_to_pdf():
    # 初始化 PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15) # 設定自動分頁，邊距 15mm
    pdf.add_page()

    # 載入字體：直接用系統的 .ttc，指定 index=0 使用標準體
    # 如果系統沒這字體，請確保路徑正確
    pdf.add_font("MSJH", style="", fname=font_path, font_index=0)
    pdf.set_font("MSJH", size=12)

    # 2. 讀取並寫入內容
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                # 使用 multi_cell 確保長句子會自動換行
                # w=0 代表寬度撐滿到邊界，h=10 是行高
                pdf.multi_cell(w=0, h=10, txt=line)
        
        # 3. 產出檔案
        pdf.output(output_file)
        print(f"✅ 成功：PDF 已儲存於：{output_file}")

    except FileNotFoundError:
        print(f"❌ 錯誤：找不到檔案 {input_file}，請確認檔案已產生。")
    except Exception as e:
        print(f"❌ 發生未知錯誤：{e}")

if __name__ == "__main__":
    convert_to_pdf()