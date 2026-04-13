handwriting_file = r"C:\CTL\AI\fontdiffuser-finetune\0_written_newline.txt" # please paste absolute path
moe_file_path = r"C:\CTL\AI\fontdiffuser-finetune\1_MOE4808_newline.txt"
big5_file_path = r"C:\CTL\AI\fontdiffuser-finetune\2_big5_newline.txt"
notosans_file_path = r"C:\CTL\AI\fontdiffuser-finetune\3_notosanschar_newline.txt"

with open(handwriting_file, "r", encoding="utf-8") as file:
    text = file.read()
with open(moe_file_path, "r", encoding="utf-8") as file:
    moe_content = "".join(file.read().split())
with open(big5_file_path, "r", encoding="utf-8") as file:
    big5_content = "".join(file.read().split())
with open(notosans_file_path, "r", encoding="utf-8") as file:
    notosans_content = "".join(file.read().split())

clean_text = "".join(text.lstrip('\ufeff')  .split()) # delete all elements which is not char
write_char_cnt = len(clean_text)
unique_characters = set(clean_text)

set_moe_file = set(moe_content)
set_big5_file = set(big5_content)
set_notosans_file = set(notosans_content)

unseen_char_simple = set_moe_file - unique_characters
unseen_char_medium = set_big5_file - set_moe_file - unique_characters
unseen_char_stronge = set_notosans_file - set_big5_file - set_moe_file - unique_characters


print("moe: ", len(set_moe_file))
print("big5: ", len(set_big5_file))
print("notosans ", len(set_notosans_file))

print("手寫字形數量: ", len(unique_characters))
print("MOE4808 - 手寫過的 字數共有: ", len(unseen_char_simple))
print("big5 - MOE4808 - 手寫過的 字數共有: ", len(unseen_char_medium))
print("notosans - big5 - MOE4808 - 手寫過的 字數共有: ", len(unseen_char_stronge))
