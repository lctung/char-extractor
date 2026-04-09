from fontTools.ttLib import TTFont

def extract_unicode_from_ttf(ttf_path):
    try:
        font = TTFont(ttf_path)
        unicode_chars = set()
        
        # 遍歷 cmap 表來提取支援的 Unicode 編碼
        for table in font['cmap'].tables:
            for codepoint in table.cmap.keys():
                unicode_chars.add(chr(codepoint))
        
        font.close()
        return sorted(unicode_chars)

    except Exception as e:
        print(f"error: {e}")
        return []

if __name__ == "__main__":
    ttf_file = "NotoSansTC-ExtraLight.ttf"  # 這裡換成你的 TTF 檔案路徑
    unicode_chars = extract_unicode_from_ttf(ttf_file)
    
    if unicode_chars:
        # 將串列合併為單一字串
        all_chars_str = "".join(unicode_chars)
        
        # 直接寫入檔案
        output_filename = "U2.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(all_chars_str)
            
        print(f"成功提取了 {len(unicode_chars)} 個不重複的字元，並已儲存至 {output_filename}")