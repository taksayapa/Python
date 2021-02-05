import os
word = {}
def menu():
    global choice
    print("พจนานุกรม\n1)เพิ่มคำศัพท์\n2)แสดงคำศัพท์\n3)ลบคำศัพท์\n4)ออกจากโปรแกรม\n")
    
def add():
    w =input("เพิ่มคำศัพท์:")
    t =input("ชนิดคำศัพท์(n,v,adj,adv):")
    m =input("ความหมาย:")
    word.update({w:{t,m}})
def view():
    print("----"*20)
    print("----"*8+"\n\tคำศัพท์ของคุณมีดังนี้\n"+"----"*8+"\nคำศัพท์ ประเภท ความหมาย")
    print("----"*20)
    for k,v in word.items():
        print(k+"           ",v)
def remove():
    r =input("พิมพ์คำศัพท์ที่ต้องการลบ:")
    q =input("คุณแน่ใจว่าต้องการลบ (y/n):")
    if q == "y":
        word.pop(r)
    else:
        print("")

while True:
    menu()
    me =int(input("เลือกรายการที่ต้องการ:"))
    if me == 1:
        add()
    elif me == 2:
        view()
    elif me == 3:
        remove()
    else:
        q =input("คุณแน่ใจว่าต้องการออกจากโปรแกรม (y/n):")
        if q == "y":
            break
        else:
            print("")