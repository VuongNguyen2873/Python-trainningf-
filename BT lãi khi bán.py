tien = (float(input("Nhập số tiền tổng doanh thu: ")))
if tien <101 :
    print ("Tiền hoa hồng nhận được là: ",tien*0.05)
elif tien<301 :
    print ("Tiền hoa hồng nhận được là: ",tien*0.1)
else:
    print ("Tiền hoa hồng nhận được là: ", tien*0.2)