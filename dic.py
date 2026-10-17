dict = {
    "name": "Harsh",
    "age": 17,
    "marks": 85.5,
    "passed": True
}

print(dict)

#students = {
    #"student1": {
       # "name": "Harsh",
        #"age": 17
    #},
    #"student2": {
       # "name": "Rahul",
       # "age": 18
   # }
#}

#print(students["student1"]["name"])    # Harsh

student = {
    "name": "Harsh",
    "age": 17,
    "course": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
student.update({"age": 18})
student.pop("age")
student.popitem()



collection = {1, 2, 3, 4, 5, "hello guys i am the great harsh rajput"}


print(collection)
print(type(collection))

collection =()

print(type(collection))