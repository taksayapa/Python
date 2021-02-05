print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรเเกรม")
f=[]
a=0
while(True):
    a+=1
    like=input("อาหารจานโปรดอันดับที่ {} คือ\t".format(a))
    f.append(like)
    if like == "exit":
        break
print("อาหารจานโปรดของคุณมีดังนี้",end="")
for x in range(1,a):
        print(x,".",f[x-1],end="")