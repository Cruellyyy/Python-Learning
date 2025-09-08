'''def decorator(func):
    def wrapper(name):
        print("Some one is about to speak loudly.")
        func(name)
        print("Someone has just speaked loudly.")
    return wrapper

def speakLoudly(name):
    print(f"{name} is speaking loudllyyyy!")

speakLoudly("Manasvi")
newFunc = decorator(speakLoudly)
newFunc("manas")'''

#better syntx
def decorator(func):
    def wrapper(name):
        print("Some one is about to speak loudly.")
        func(name)
        print("Someone has just speaked loudly.")
    return wrapper

@decorator
def speakLoudly(name):
    print(f"{name} is speaking loudllyyyy!")

@decorator
def speaking(name):
    print("speaking")

speakLoudly("Manasvi")
speaking("hfiuh")


