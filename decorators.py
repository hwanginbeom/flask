def hello(f):
    def greeting():
        print("^___^")
        f()
        print("ㅠ  ㅠ")
    return greeting
    
@hello
def korean():
    print("안녕하세요")
    
@hello
def english():
    print("hello")
    
korean()
english()
#a=hello(korean)
#a()