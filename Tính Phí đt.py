phut = (float(input("Nhập số phút đã gọi trong tháng: ")))
if phut <51:
    print ("Cước điện thoại tháng này là: ",25+0.6*phut)
elif phut < 201:
    print ("Cước điện thoại tháng này là: ",25+0.4*phut)
else:
    print ("Cước điện thoại tháng này là: ",25+0.2*phut)