def greet():
    print("Hello Harsh")

greet()

#def → function banane ke liye keyword
#greet → function ka naam
#() → parameters ke liye
#: → function ka block start
#greet() → function ko call karna
def greet():
    print("Hello")

greet()
greet()
greet()

def greet(name):
    print("Hello", name)

greet("Harsh")
greet("Rahul")

def add(a, b):
    print(a + b)

add(10, 20)

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

def add(a, b):
    return a + b

x = add(10, 20)
y = x * 2

print(y)

