tx=(float(input("Nhập trung bình điểm kiểm tra thường xuyên: ")))
gk=(float(input("Nhập điểm kiểm tra giữa kì: ")))
cc=(float(input("Nhập điểm kiểm ta cuối kì: ")))
tbc= (tx+gk*2+cc*3)/6
if tbc < 5:
    print ("Thuộc hạng F")
elif tbc < 7:
    print ("Thuộc hạng C")
elif tbc <9 :
    print ("Thuộc hạng B")
else:
    print ("Thuộc hạng A")