from QuanLySinhVien import QuanLySinhVien

qLsv = QuanLySinhVien()
while (1):
    print("CHUONG TRINH QUAN LY SINH VIEN")
    print("******************************MENU******************************")
    print("*** 1. Them sinh vien.")
    print("*** 2. Cap nhat thong tin sinh vien boi ID.")
    print("*** 3. Xoa sinh vien theo ID.")
    print("*** 4. Tim kiem sinh vien theo ten.")
    print("*** 5. Sap xep danh sach sinh vien theo diem trung binh (GPA).")
    print("*** 6. Sap xep danh sach sinh vien theo ten chuyen nganh.")
    print("*** 7. Hien thi danh sach sinh vien.")
    print("*** 8. Thoat")
    print("***************************************************************")
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("1. Them sinh vien.")
        qLsv.nhapSinhVien()
        print("Them sinh vien thanh cong!")
    elif (key == 2):
        if (qLsv.soLuongSinhVien() > 0):
            print("2. Cap nhat thong tin sinh vien.")
            print("nhập mã số sinh viên cần cập nhật: ")
            ID = int(input())
            qLsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 3):
        if (qLsv.soLuongSinhVien() > 0):
            print("3. Xoa sinh vien.")
            print("nhap id sinh viên cần xóa")
            ID = int(input())
            if (qLsv.deleteByID(ID)):
                print("Sinh vien co id = ", ID, " da bi xoa.")
            else:
                print("Sinh vien co id = ", ID, " khong ton tai.")
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 4):
        if (qLsv.soLuongSinhVien() > 0):
            print("4. Tim kiem sinh vien theo ten.")
            print("Nhap ten de tim kiem: ")
            name = input()
            searchResult = qLsv.findByName(name)
            qLsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 5):
        if (qLsv.soLuongSinhVien() > 0):
            print("5. Sap xep sinh vien theo diem trung binh (GPA).")
            qLsv.sortByDiemTB()
            qLsv.showSinhVien(qLsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 6):
        # (Chưa hoàn thành trong tài liệu, thêm placeholder)
        print("6. Sap xep sinh vien theo ten chuyen nganh.")
        if (qLsv.soLuongSinhVien() > 0):
            qLsv.sortByName()  # Giả sử dùng sortByName làm placeholder
            qLsv.showSinhVien(qLsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 7):
        if (qLsv.soLuongSinhVien() > 0):
            print("7. Hien thi danh sach sinh vien.")
            qLsv.showSinhVien(qLsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    else:
        break