import calc

def test_add():
    if calc.add(2, 3) == 5:
        print("True")
    else:
        print("False")

def test_sub():
    if calc.sub(5, 2) == 3:
        print("True")
    else:
        print("False")
        
def test_mul():
    if calc.mul(2, 3) == 6:
        print("True")
    else:
        print("False")

def test_div():
    if calc.div(6, 3) == 2:
        print("True")
    else:
        print("False")


test_add()
test_sub()
test_mul()
test_div()