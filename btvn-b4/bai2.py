a={203,204,250,242,256,235,643}
b={204,304,245,234,523,543,242}
print(a)
print(b)
c=a|b
if c=={0}:
    print("không có sinh viên nào đăng ký học ở cả 2 bàn")
else :
    print("có sinh viên nào đăng ký học ở cả 2 bàn")
print("danh sách mã sinh viên đăng ksy cả ở 2 bàn ",c)
print("danh sách sinh viên đăng ký ở bàn 1 mà không đăng ký ở bàn 2 ",a-b)
