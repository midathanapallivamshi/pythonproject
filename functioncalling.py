print("here i am creating call the function")
def add():
    print("i am add operation")
    sub()
def sub():
    print("i am subaraction function")

def mul():
    print("i am multilication operation")
def div():
    print(" iam div operation")
    mul()
add()
sub()
mul()
div()
