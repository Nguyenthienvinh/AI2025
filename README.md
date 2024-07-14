# HIT_PYTHUN_PUBLIC_2024
Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

Python là một ngôn ngữ thông dịch 

Vì:
*Không cần biên dịch trước: Không cần phải biên dịch toàn bộ chương trình thành mã máy trước khi chạy, mà bạn có thể thực thi từng dòng lệnh một.
*Cách thức hoạt động: Mã nguồn Python được chuyển đổi thành bytecode (mã trung gian) bởi trình thông dịch Python (CPython là phiên bản thực thi tiêu chuẩn). Bytecode này sau đó được thực thi trên máy ảo Python (Python Virtual Machine - PVM).
*Tiện lợi trong phát triển: Cho phép các lập trình viên thực hiện và kiểm tra từng phần của chương trình mà không cần chờ quá trình biên dịch đầy đủ như các ngôn ngữ biên dịch như C++ hay Java.
*Tính linh hoạt và dễ sử dụng: Python dễ học và dễ sử dụng hơn những ngôn ngữ yêu cầu biên dịch trước như C++ hay Java.


Các kiểu dữ liệu trong Python:
Số (Numbers):
int: Số nguyên (e.g., 1, -3, 42)

float: Số thực (e.g., 3.14, -0.001, 2.0)
complex: Số phức (e.g., 1+2j, -3j)
Chuỗi (String): Đại diện cho dãy ký tự (e.g., "Hello", 'Python')

Danh sách (List): Danh sách các phần tử có thể thay đổi được (e.g., [1, 2, 3], ['apple', 'banana'])

Tuple: Danh sách các phần tử không thể thay đổi (e.g., (1, 2, 3), ('a', 'b', 'c'))

Từ điển (Dictionary): Cặp key-value (e.g., {'name': 'John', 'age': 25})

Set: Tập hợp các phần tử không trùng lặp (e.g., {1, 2, 3})

Boolean: Chỉ có hai giá trị là True và False.


Các toán tử trong Python:

Toán tử số học: +, -, *, /, //, %, **

Toán tử so sánh: ==, !=, >, <, >=, <=

Toán tử logic: and, or, not

Toán tử gán: =, +=, -=, *=, /=, %=, **=, //=

Toán tử bit: &, |, ^, ~, <<, >>
Mệnh đề điều kiện và vòng lặp

Mệnh đề điều kiện (if-elif-else):

if điều_kiện:

    thực_thi_khối_lệnh

elif điều_kiện_khác:

    thực_thi_khối_lệnh_khác

else:

    thực_thi_khối_lệnh_cuối

Vòng lặp:

for:

for biến in dãy:

    thực_thi_khối_lệnh

while:

while điều_kiện:

    thực_thi_khối_lệnh

Kiểu dữ liệu True, False


Boolean: Kiểu dữ liệu chỉ có hai giá trị là True và False. Trong Python, các giá trị này được sử dụng trong các mệnh đề điều kiện và toán tử logic. is_active = True

has_permission = False

if is_active and has_permission:

    print("Access granted")

else:

    print("Access denied")