'''
def avg(marks):
    assert len(marks) != 0, "the list is empty."
    return sum(marks)/len(marks)


marks1 = [67,59,86,75,92]
print("The average of marks1:",avg(marks1))
marks2 = [10,20,30,40]
print("the average of marks2:",avg(marks2))


'''




list123=[1,2,33,7,9,0]
x=6
assert x not in list123," x is not in list "

assert x in list123 , " x is in list"