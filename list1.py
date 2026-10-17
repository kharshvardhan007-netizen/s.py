fruits = ["apple","bnana" , "mango"]
print(fruits)

#append()
fruits = ["Apple", "Banana"]
fruits.append("Mango")

print(fruits)

#insert()
fruits.insert(1, "Mango")
print(fruits)

fruits.remove("Banana")
fruits.pop(1)

numbers = [5, 2, 8, 1]
numbers.sort()

print(numbers)

numbers.reverse()


#tuples
student = ("Harshu", 17, "CSE")

print(student[0])    # Harshu
print(student[1])    # 17
print(student[2])    # CSE

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

numbers = (10, 20, 30, 40)

print(numbers.index(30))

movies =[]
mov1= input("enter 1st movie:")
mov2= input("enter 2nd movie:")
mov3= input("enter 3rd movie:")


movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

list1 = [1, 2, 1]
list2 = [3, 4, 5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print(" palindrome")
else:
    print("not palindrome")

 