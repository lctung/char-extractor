import re

def extract_big5_characters(file_path):
    big5_list = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 跳過註解行或空行
            if line.startswith('#') or not line.strip():
                continue
            
            # 使用 split 分割欄位 (通常是 Tab 或空格分隔)
            parts = line.split()
            
            # 判斷是否為有效的條目：
            # 1. 至少有兩欄
            # 2. 第二欄必須是 Unicode (0x 開頭)，排除 "DBCS LEAD BYTE"
            if len(parts) >= 2 and parts[1].startswith('0x'):
                big5_hex = parts[0]
                unicode_hex = parts[1]
                
                # 將十六進位字串轉為實際的中文字元
                try:
                    # 邏輯：將 0x4E00 轉為整數再轉為 Unicode 字元
                    char = chr(int(unicode_hex, 16))
                    big5_list.append(char)
                except ValueError:
                    continue
                    
    return big5_list

# 執行提取
file_name = 'medium_baseline.txt'  # 請確認檔案路徑正確
all_chars = extract_big5_characters(file_name)
output_filename = 'extracted_big5.txt'
# 顯示前 10 個抓到的字
for item in all_chars[:10]:
    print(f"字元: {item}")

print(f"\n總共抓取到 {len(all_chars)} 個字元")

with open(output_filename, 'w', encoding='utf-8') as f:
    for i in range(len(all_chars)):
        f.write(all_chars[i] + '\n')