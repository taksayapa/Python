shop_list=[]
amount=[0,0,0,0,0]
price=[150,200,180,155,135]
def out_item():
    n=0
    while(True):
        print("\tสินค้าในตะกร้ามีดังนี้")
        for i in shop_list:
            n+=1
            print("\t"+str(n)+"."+i)
        n=0
        c=int(input("เลือกลำดับสินค้าที่จะหยับออก หรือพิมพ์ -1 เพื่อออก:"))
        try:
            if c<=len(shop_list) and c!=-1:
                shop_list.pop(c-1)
            elif c==0 and c<=len(shop_list) and c!=-1:
                shop_list.pop(c)
            elif c==-1:
                break
        except:
            print("กรุณากรอกลำดับสินค้าให้ถูกต้อง")
def list_item():
    print("\tรายการสินค้า")
    print("-----"*20)
    print("1.You n Me 150 ฿")
    print("2.Calls in Love 200฿")
    print("3.reddd 180฿")
    print("4.Eat Me!! 155฿")
    print("5.Moon Mood 135฿")
def pick_item():
    c=0
    while(True):
        print("1.You n Me")       
    print("2.Calls in Love ")
    print("3.reddd ")
    print("4.Eat Me!! ")
    print("5.Moon Mood ")
    c=(input("เลือกหยิบสินค้าหมายเลข:"))
    try:
        if int(c)==1 or c=="1":
            shop_list.append("You n Me")
        elif int(c)==2 or c=="2":
            shop_list.append("Calls in Love")
        elif int(c)==3 or c=="3":
            shop_list.append("reddd")
        elif int(c)==4 or c=="4":
            shop_list.append("Eat Me!!")
        elif int(c)==5 or c=="5":
            shop_list.append("Moon Mood")
        elif int(c)==6 or c=="6":
            break
        else:
            print("กรุณากรอกหมายเลขให้ถูกต้อง")
            pass
        except:
            print("กรุณากรอกหมายเลขให้ถูกต้อง")
            pass
def show_item():

    for i in shop_list:
        if i == "You n Me":
            amount[0]+=1
        elif i =="Calls in Love":
            amount[1]+=1
        elif i =="reddd":
            amount[2]+=1
        elif i =="Eat Me!!":
            amount[3]+=1      
        elif i =="Moon Mood":
            amount[4]+=1
amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
pricettt=amount[0]*150+amount[1]*200+amount[2]*180+amount[3]*155+amount[4]*135
print("")
print("{0:_<10}{1}{0:_<10}".format("","สินค้าที่คุณได้หยิบไปมีดังนี้"))
print("{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}".format("","สินค้า","จำนวน","ราคา"))
print("{0:_<38}".format(""))
if amount[0]!=0:
    print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","You n Me",str(amount[0]),str(amount[0]*150)))
if amount[1]!=0:
    print("{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","Calls in Love",str(amount[1]),str(amount[1]*200)))
if amount[2]!=0:
    print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","reddd",str(amount[2]),str(amount[2]*180)))
if amount[3]!=0:
    print("{0:.<6}{1}{0:.<8}{2}{0:.<9}{3}{0:.<10}".format("","Eat Me!!",str(amount[3]),str(amount[3]*155)))
if amount[4]!=0:
   print("{0:.<6}{1}{0:.<3}{2}{0:.<9}{3}{0:.<10}".format("","Moon Mood",str(amount[4]),str(amount[4]*135)))
print("{0:_<38}".format(""))
print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricettt)))
print("")
print("\tโปรแกรมร้านหนังสือดรอเพลย์ออนไลน์")
print("----"*20)
while(True):
    print("1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม")
    print('')
    ch=input("กรุณาเลือกทำรายการ")
    if ch =="1":
        list_item()
    elif ch=="2":
        pick_item()
    elif ch=="3":
        show_item()
    elif ch=="4":
        out_item()
     elif ch=="5":
        ch=input("ต้องการออกจากโปรแกรมใช่หรือไม่ y/n:")
        if ch =='y':
            break
        elif ch == 'n'
            continue