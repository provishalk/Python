import docx2txt
MY_TEXT = docx2txt.process("input.docx")
str_array = MY_TEXT.split()
search_text = "the"
count = 0
for i in str_array:
    if i == search_text:
        count += 1
print(f"word =>'{search_text}'<= occurred {count}  times")