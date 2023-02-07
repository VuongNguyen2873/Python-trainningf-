l=int(input('Nhập số tiền lương của nhân viên: '))
if l<7 :
    print("Thuế cần thu là: ",l*0.1)
    print("Lương cơ bản: ",l*0.9)
elif l<15:
    print("Thuế cần thu là: ",l*0.2)
    print("Lương cơ bản: ",l*0.8)
else:
    print("Thuế cần thu là: ",l*0.3)
    print("Lương cơ bản: ",l*0.7)


