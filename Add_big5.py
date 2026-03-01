# -*- coding: utf-8 -*-
import os

# 設定目標路徑
target_dir = r"Nicktest\Python-PDF-Encoding-Toolkit\Add_big5"
file_path = os.path.join(target_dir, "big5.txt")

# 寫入 Big5 測試檔案 預設為ANSI格式
test_content = "這是一段繁體中文測試：電腦、軟體、編碼。"

try:
    with open(file_path, 'w', encoding='big5') as f:
        f.write(test_content)
    print(f"✅ 測試檔已成功生成於：{file_path}")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")


