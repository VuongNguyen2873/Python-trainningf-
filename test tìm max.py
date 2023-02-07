n = (int(input("Bạn muốn tìm số lớn nhất của bao nhiêu số? :")))
timmax= []
for x in range(n):
    t=(float(input("Nhập giá trị: ")))
    timmax.append(t)
print('>Giá trị lón nhất trong list là: ', max(timmax))