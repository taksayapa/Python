print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรเเกรม")
list=[]
i=1
x=0
z=1
while (True):
    x = input("อาหารโปรดอันดับที่ " + str(i) + "คือ  ") # str = ตัวเลข
    list.append(x)
    i+=1
    if x == "exit" :
        print("\n อาหารสุดโปรดของคุณมีดังนี้")
        list.pop()
        break # หยุดการทำงาน
print(list)