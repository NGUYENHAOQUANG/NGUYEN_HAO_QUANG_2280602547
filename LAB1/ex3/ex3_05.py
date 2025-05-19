def count_item(lst):
    count_dict = {}
    for items in lst:
        if items in count_dict:
            count_dict[items] += 1
        else:
            count_dict[items] = 1
    return count_dict

input_string = input("nhập danh sách các từ: ")
word_list = input_string.split()


solansuaathien = count_item(word_list)
print("số lần xuất hiện của các phẩn tử: ",solansuaathien)