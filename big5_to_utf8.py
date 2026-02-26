# -*- coding: utf-8 -*-
# 讀取 Big5，寫入 UTF-8
# 加入 errors='ignore' 可以跳過非法字元，避免程式崩潰
try:
    with open('big5.txt', 'r', encoding='big5', errors='ignore') as f_in:
        content = f_in.read()

    with open('utf8.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(content)
        
    print("✅ 轉換成功！檔案已儲存為 utf8.txt")

except FileNotFoundError:
    print("❌ 錯誤：找不到 big5.txt，請確認檔案是否存在。")