employee_quantity = int(input("\nNhập số lượng nhân viên: "))
for employee in range(employee_quantity):
    employee_name = input("\nNhập tên nhân viên: ")
    work_number = int(input("Nhập số ngày làm việc: "))
    if work_number < 0 or work_number > 22:
        print("Dữ liệu không hợp lệ")
        continue
    
    if work_number == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
    elif work_number >= 18:
        print(f"{employee_name}: ", end="")
        for pattern in range(work_number):
            print(f"* ", end="")
        print()
        print("Làm việc chăm chỉ")
    elif work_number < 10:
        print(f"{employee_name}: ", end="")
        for pattern in range(work_number):
            print(f"* ", end="")
        print()
        print("Làm việc ít")
    else:
        print(f"{employee_name}: ", end="")
        for pattern in range(work_number):
            print(f"* ", end="")
        print()
        print("Làm việc bình thường")