def reverse(lst):
    return lst[::-1]

input_list = input("nhập danh sách các số:")
number = list(map(int,input_list.split(" ")))

list_reverse = reverse(number)
print("danh sach dao nguoc la: ",list_reverse)