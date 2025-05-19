def create_tuple_list(lst):
    return tuple(lst)

input_list= input("nhập danh sách các số:")
numbers = list(map(int,input_list.split(' ')))

my_tuple = create_tuple_list(numbers)
print("danh sách ban đầu là: ", numbers)
print("danh sách tuple list là: ", my_tuple)