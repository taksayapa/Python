print("กรุณากรอกจำนวนครั้งการรับค่า ")
num=int(input(""))
i=0
sum=0
while(i < num) :
    number=int(input("กรอกตัวเลข"))
    i+=1
    sum = sum + number
print("ผลรวมค่าที่รับมาทั้งหมด :"+str(sum))