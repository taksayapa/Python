listshop=[0,0,0,0,0]
cost=[5,10,50,2,20]
def menu():
    global choice
    print('ดรอเพลย์ออนไลน์\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าในตะกร้า\n 3.แสดงรายจำนวนและราคาสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
    choice = input('กรุณาเลือกทำรายการ : ')

def costmenu():
    print('\n1.ปากกา ราคา 5 บาท\n 2.แว่น ราคา 10 บาท\n 3.สมุด ราคา 50 บาท\n 4.ลูกอม ราคา 2 บาท\n 5.หนังสือ ราคา 20 บาท\n')

def pickmenu():
    global pick
    print('\nรายการสินค้า\n 1.ปากกา\n 2.แว่น\n 3.สมุด\n 4.ลูกอม\n 5.หนังสือ')
    pick = int(input('เลือกหยิบสินค้าหมายเลข: '))
    if pick  == 1:
        listshop[0] += 1
    elif pick == 2:
        listshop[1] += 1
    elif pick == 3:
        listshop[2] += 1
    elif pick == 4:
        listshop[3] += 1
    elif pick == 5:
        listshop[4] += 1
    
def allpick():
    list_fruit = ['ปากกา','แว่น','สมุด','ลูกอม','หนังสือ']
    list_cost =[5,10,50,2,20]
    print("{0:-<10}{1:-<10}{2:-<10}{3}".format('สินค้า','ราคา','จำนวน','ยอดรวม'))
    for i in range(0,5):
        print("{0:-<10}{1:-<10}{2:-<10}{3}".format(list_fruit[i], list_cost[i], listshop[i], listshop[i]*list_cost[i]))

def outpick():
    print('รายการสินค้า\n 1.ปากกา\n 2.แว่น\n 3.สมุด\n 4.ลูกอม\n 5.หนังสือ')
    outpick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
    if outpick  == 1:
        listshop[0] -= 1
    elif outpick == 2:
        listshop[1] -= 1
    elif outpick == 3:
        listshop[2] -= 1
    elif outpick == 4:
        listshop[3] -= 1
    elif outpick == 5:
        listshop[4] -= 1

while True:
    menu()
    if choice == '1':
        costmenu()
    elif choice == '2':
        pickmenu()
    elif choice == '3':
        allpick()
    elif choice == '4':
        outpick()
    elif choice == '5':
        ch = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if ch == 'y':
            break
        elif ch == 'n':
            continue