def hello():

    print("It's worked")
    return "hello"

print(hello())

greet = hello
print(greet)



def hello(name = "Jack"):

    print("Hello fuction become executed!")

    def greet():
        return '\t greet inside the hello!'
    return greet()
print(hello())

