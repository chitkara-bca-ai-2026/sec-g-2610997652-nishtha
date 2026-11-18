import os

while True:
    print("1.Display Logs.\n2.Add Log\n3.Exit")
    ch=input("Enter choice: ")

    if ch=="1":
        if os.path.exists("logs.txt"):
            f=open("logs.txt","r")
            for line in f:
                print(line)
    elif ch=="2":
        log=input("Enter log: ")
        f=open("logs.txt","a")
        f.write(log+"\n")
        f.close()

    elif ch=="3":
        break

    else:
        print("INVALID")
