def P1(n):
    print("Parent")
    def C1():
        print("Child2")
        return 10
    print("Parent1")
    def C2():
        print("Child2")
    print("Parent2")
    if n == 1:
        return C1
    else:
        return C2

def P2():
    print("dummy")