import math
a = (float(input("Nhập hệ số a: ")))
b = (float(input("Nhập hệ số b: ")))
c = (float(input("Nhập hệ số c: ")))

if a ==b == 0 :
    print("Vô nghiệm vì a=b")
elif a==0:
    print("Phương trình có nghiệm là",-b/a)
else:
    d = b**2-4*a*c
    if d==0:
        print ("Phương trình có nghiệm kép X1 = X2 =",-b/2*a)
    elif d>0:
        print ("Nghiệm thứ nhất x1 là: ",(-b+math.sqrt(d))/2*a)
        print ("Nghiệm thứ nhất x2 là: ",(-b-math.sqrt(d))/2*a)
    else:
        print ("Vô nghiệm do delta < 0")
