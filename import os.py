import os
choice=0
filename=""

def menu():
    global choice
    print("Menu\n 1.Open Write\n 2.Open Notepad\n 3.Exit")
    choice=input("Select Menu:")


    def opennotepad():
        filename="C:\Windows\\notepad.exe"
        print("Memorandum writing %s" %filename)
        os.system(filename)

    def openwrite():
        filename="C:\Windows\\write.exe"
        print("Write  %s" %filename)
        os.system(filename)

while True:
    menu()
    if choice =="1":
        openwrite()
    elif choice =="2":
        opennotepad()
    else:
        break