sogiolam = float(input("nhập số giờ làm mỗi tuần: "))
luonggio = float(input("nhập thù lao trên mỗi giờ làm tiều chuẩn: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
print(f"số tiền thực lĩnh của nhân viên là: {thuclinh}")