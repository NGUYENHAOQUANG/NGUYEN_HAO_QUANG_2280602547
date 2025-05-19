def sum_even_number(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhập danh sách các số:")
number = list(map(int,input_list.split(" "))) # map áp dụng thay đổi cho từng phần tử trong mảng mà không cần vòng lập

tong_chan = sum_even_number(number)
print("tổng các số chẵn trong danh sách là: ", tong_chan)