def access_element_list(lst):
    frist = lst[0]
    last = lst[-1]
    return frist, last

input_tuple = eval(input("nhập tuple: ví dụ(1,2,3)")) # eval kiểm tra input trả về có phải là biểu thức python hợp lệ hay không
môt , hai = access_element_list(input_tuple) # tự động ánh xạ

print("phần tử đầu tiên: ",môt)
print("phần tử cuối cùng: ", hai)