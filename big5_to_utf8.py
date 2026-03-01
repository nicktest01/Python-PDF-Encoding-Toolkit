# 讀取 Big5，寫入 UTF-8
import os

#設定路徑
source_dir = r"Nicktest\Python-PDF-Encoding-Toolkit\Add_big5"
source_file = os.path.join(source_dir, "big5.txt")

output_dir = r"Nicktest\Python-PDF-Encoding-Toolkit\Big5_to_utf8"
output_file = os.path.join(output_dir, "big5_utf8.txt")

#確保目標資料夾存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"📁 已建立目錄：{output_dir}")

try:
    # 3. 讀取 Big5 檔案
    # 使用 errors='replace' 避免因少數特殊字元導致轉檔失敗
    with open(source_file, 'r', encoding='big5', errors='replace') as f:
        content = f.read()

    # 4. 寫入 UTF-8 檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 轉檔成功！")
    print(f"📄 來源：{source_file} (Big5)")
    print(f"🚀 目標：{output_file} (UTF-8)")

except FileNotFoundError:
    print(f"❌ 找不到來源檔案，請確認路徑是否正確：{source_file}")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")