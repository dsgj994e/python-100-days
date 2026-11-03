
#def greet():
#    print("Hello")
#    print("Howdy")
#    print("Salutations")
#greet()

#def greet_with_name(name):
#    print(f"Hello, {name}")
#    print(f"How do you do, {name}?")
#greet_with_name("Douglas")

# parameter = name ^
# argument = "Douglas" ^

def greet_with(name,location):
    print(f"Hello, {name}")
    print(f"How is the weather in {location}?")
greet_with("Douglas","Chicago")
# positional argument ^
greet_with(location = "Wakefield",name = "Donald" )
#