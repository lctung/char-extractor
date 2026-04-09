from fontTools.ttLib import TTFont
import json
def extract_unicode_from_ttf(ttf_path):
    font = TTFont(ttf_path)
    unicode_chars = set()
    
    for table in font['cmap'].tables:
        for codepoint in table.cmap.keys():
            unicode_chars.add(chr(codepoint))
    
    font.close()
    return sorted(unicode_chars)

if __name__ == "__main__":
    ttf_file = "NotoSansTC-ExtraLight.ttf"  # 這裡換成你的 TTF 檔案路徑
    unicode_chars = extract_unicode_from_ttf(ttf_file)
    print("Extracted Unicode characters:")
    print("".join(unicode_chars))

# 使用列表推導式將字符串分割為單個字符的列表
chinese_characters = [char for char in unicode_chars]
with open("U2.txt", 'w', encoding='utf-8') as f:
    f.write(''.join(chinese_characters))


