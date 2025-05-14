print("nhập dòng văn bản(nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == "done":
        break
    lines.append(line)
print("\n các dòng dẫ nhập sau khi chuyển thành chữ hoa:")
for line in lines:
    print (line.upper())
    