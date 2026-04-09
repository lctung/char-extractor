Big5_ranges = {
    "Graphical characters": (0xA140, 0xA3BF),
    "Frequently used characters": (0xA440, 0xC67E),
    "Less frequently used characters": (0xC940, 0xF9D5)
}

def generate_big5_extracted_text():
    count = 0
    text_content = ""
    for category, (start, end) in Big5_ranges.items():
                
        chars_in_category = []
        # 分解出高位元組與低位元組
        start_high, start_low = start >> 8, start & 0xFF
        end_high, end_low = end >> 8, end & 0xFF
        
        for h in range(start_high, end_high + 1):
            for l in range(0x40, 0xFF): # Big5 低位元組範圍是 0x40-0x7E, 0xA1-0xFE
                # 檢查是否在指定區間內
                if (h == start_high and l < start_low) or (h == end_high and l > end_low):
                    continue
                
                # 排除非 Big5 定義的低位元組區間 (0x7F-0xA0 是空的)
                if 0x40 <= l <= 0x7E or 0xA1 <= l <= 0xFE:
                    try:
                        # 將數值轉成 Bytes 再解碼為 Unicode 字串
                        big5_bytes = bytes([h, l])
                        char = big5_bytes.decode('cp950')
                        chars_in_category.append(char)
                        count += 1
                    except UnicodeDecodeError:
                        continue # 遇到未定義的空位就跳過
        
        text_content += "".join(chars_in_category)
    return text_content, count

def save_to_file(filename="big5.txt", ):
    text, count = generate_big5_extracted_text()
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"成功將 Big5 內容提取並轉換為 Unicode 寫入 {filename}")
    print(f"共有 {count} 個字")

if __name__ == "__main__":
    save_to_file()