import os
grocery=[]
amount=[0,0,0,0,0]
price=[10,15,20,25,30]
print('\tโปรแกรมร้านDRAWPLAYออนไลน์\n','------'*20)
def menu():
    global choice 
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าใส่ตะกร้า\n3.แสดงจำนวนและราคาที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ออกจากโปรแกรม\n')
    choice = input('กรณาเลือกทำรายการ:')

def a():
    print('\tรายการสินค้า\n','------'*20,'\n','\t1.redd 10฿\n2.bluee 15฿\n3.greenn 20฿\n4.pinkk 25฿\n5.yelloww 25฿\n')

def b():
    color = 0
    while(True):
        print('\t1.redd\n2.bluee\n3.greenn\n4.pinkk\n5.yelloww\n6.ออกจากฟังก์ชัน')
    color = input('เลือกสินค้า:')
    try:
        if int(color)==1 or color=='1':
            grocery.append('redd')
        elif int(color)==2 or color=='2':
            grocery.append('bluee')
        elif int(color)==3 or color=='3':
            grocery.append('greenn')
        elif int(color)==4 or color=='4':
            grocery.append('pinkk')
        elif int(color)==5 or color=='5':
            grocery.append('yelloww')
        elif int(color)==6 or color=='6':
            break
        else:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
    except:
        print('กรุณากรอกหมายเลขให้ถูกต้อง')
        pass
def c():
    for i in grocery:
        if i == 'redd':
            amount[0]+=1
        elif i == 'bluee':
            amount[1]+=1
        elif i == 'greenn':
            amount[2]+=1
        elif i == 'pinkk':
            amount[3]+=1
            