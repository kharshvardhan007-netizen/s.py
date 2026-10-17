#f = open ("demo.txt", "w")
#f.write("Hello, World!")
#f.close()


#with open ("demo .txt", "w") as f :
   #f.write("Hello, World!")
#

with open ("pratice.txt", "w") as f :
    f.write("hii this is harsh ")
    f.write("fkdfvflk")

word = "learning"
with open ("pratice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")



def check_word_for_line ():
    word = "pyq"
    data = true
    line_no = 1
    with open("pratice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1

....retur -1

print(check_for_line())

with open ("pratice.txt.","r")as f:
    for i in range (len(data)):
        if(data[i]==","):
            print(num)
            num = ""
        else:
            num += data[i]



