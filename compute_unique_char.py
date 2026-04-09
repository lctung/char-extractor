manuscript_content_file = r"D:/NTUT/AI/text/write.txt" # please paste absolute path
moe_file = r"D:/NTUT/AI/text/MOE4808.txt"
notosans_file = r"D:/NTUT/AI/text/notosanschar.txt"
big5_file = r"D:\NTUT\AI\Font-Project\Extract_Font\big5.txt"

with open(manuscript_content_file, "r", encoding="utf-8") as file:
    text = file.read()
with open(moe_file, "r", encoding="utf-8") as file:
    moe_file = file.read()
with open(notosans_file, "r", encoding="utf-8") as file:
    notosans_file = file.read()
with open(big5_file, "r", encoding="utf-8") as file:
    big5_file = file.read()

clean_text = "".join(text.lstrip('\ufeff').split()) # delete all elements which is not char
write_char_cnt = len(clean_text)

set_moe_file = set(moe_file)
set_notosans_file = set(notosans_file)
set_big5_file = set(big5_file)

unique_characters = set(clean_text)

unseen_char_simple = set_moe_file - unique_characters
unseen_char_medium = set_big5_file - set_moe_file - unique_characters
unseen_char_stronge = set_notosans_file - set_big5_file - set_moe_file - unique_characters


unique_char_cnt = len(unique_characters)
unseen_char_simple_cnt = len(unseen_char_simple)
unseen_char_medium_cnt = len(unseen_char_medium)
unseen_char_stronge_cnt = len(unseen_char_stronge)

# print(clean_text)
# print("----------------------------")
# print(unique_characters)
# print("----------------------------")
print("big5: ", len(set_big5_file))
print("notosans ", len(notosans_file))
print("moe: ", len(moe_file))
# print("手寫字數: ", write_char_cnt)
print("字形數量: ", unique_char_cnt)
print("MOE4808 - 手寫過的 字數共有: ", unseen_char_simple_cnt)
print("big5 - MOE4808 - 手寫過的 字數共有: ", unseen_char_medium_cnt)
print("notosans - big5 - MOE4808 - 手寫過的 字數共有: ", unseen_char_stronge_cnt)
# print(clean_text)

# output = r"D:\NTUT\AI\notosanschar_newline.txt"
# with open(output, "w", encoding="utf-8") as file:
#     for char in clean_text:
#         file.write(char)