def delete_element(lst, key):
    if key in lst:
        del lst[key]  # Xóa phần tử theo khóa
        return True
    else:
        return False
key = 'b'
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = delete_element(my_dict, key)
if result:
    print("Xóa phần tử thành công:", my_dict)
else:
    print("Xóa phần tử không thành công, không tìm thấy phần tử")