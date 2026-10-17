#take a number from user and check it's positive , negative or zero 
#num = int(input("enter a number:"))

#if num >0:
   # print("positive number")
#elif num <0:
#    print("negative number")
#else:
  #  print("zero")


#num = int(input("enter a num"))

#if num %2==0:
    #print("even number")
#else:
    #print("odd number")

num = int(input("Enter a number"))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

mark = int(input("Enter mark"))
if mark >= 90:
    print("Excellent")
elif mark >= 60:
    print("Good")
elif mark >= 40:
    print("Pass")
else:
    print("Fail")