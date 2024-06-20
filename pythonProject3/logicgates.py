def OR(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False

print("A=True|B=True|A OR B=True", OR(1,1))
print("A=False|B=False|A OR B=False",OR(1,0))
print("A=False|B=False|A OR B=False",OR(0,1))
print("A=False|B=False|A OR B=False",OR(0,0))