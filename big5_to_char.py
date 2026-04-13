import re

def extract_big5_characters(file_path):
    big5_list = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            
            if line.startswith('#') or not line.strip():
                continue
            
            parts = line.split()
            
            if len(parts) >= 2 and parts[1].startswith('0x'):
                big5_hex = parts[0]
                unicode_hex = parts[1]
                
                try:
                    # 邏輯：將 0x4E00 轉為整數再轉為 Unicode 字元
                    char = chr(int(unicode_hex, 16))
                    big5_list.append(char)
                except ValueError:
                    continue
                    
    return big5_list

file_name = 'big5_range.txt'  # 請確認檔案路徑正確
all_chars = extract_big5_characters(file_name)
output_filename = '2_big5_newline.txt'

# 顯示前 10 個抓到的字
for item in all_chars[:10]:
    print(f"字元: {item}")

print(f"\n總共抓取到 {len(all_chars)} 個字元")

with open(output_filename, 'w', encoding='utf-8') as f:
    for i in range(len(all_chars)):
        f.write(all_chars[i] + '\n')