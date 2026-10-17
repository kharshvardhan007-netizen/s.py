str = " i am studying python from my book  "
print(str.endswith("book"))

str = " i am studying python from my book  "
print(str.replace("o","a"))

str = " i am studying python from my book  "
print(str.find("o"))

str = " i am studying python from my book  "
print(str.count("from"))

#wap to input users first name and print its lenth
first_name = input("Enter your first name: ")
print("Length of your first name is:", len(first_name))

#wap to find the occurrence of '$'in a string .
string = input("Enter a string: ")
print("Occurrence of '$' in the string is:", string.count('$'))


#wap to check if a number enterred by the user is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

a= int (input("Enter first number: "))
b= int (input("Enter second  number: "))
c= int (input("Enter third  number: "))

if (a >= b and a>=c):
    print("first number is largest",a)
elif(b >=c):
    print("second number is largest",b)
else:
    print("third is largest",c)

#wap to check if a number is a multiple of 7 or not 
x = int(input("enter number:"))
if (x %7 == 0):
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")