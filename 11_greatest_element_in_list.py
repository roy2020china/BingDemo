# Define a procedure, greatest, 
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
# 定义一个名为greatest的函数，传入一个正数列表，返回其中数值最大的正数。如果传入的是空列表，那么返回值应当为0。


# Solution 1 解决方案1
def greatest(list_of_numbers):
    # num = list_of_numbers[0]
    if not list_of_numbers:
        return 0
    num = list_of_numbers[0]
    for each_num in list_of_numbers:
        num = greater(num, each_num)
    return num


def greater(a, b):
    if a > b:
        return a
    else:
        return b

    
# Solution 2 解决方案2    
def greatest(p):
    bigger = 0
    for i in p:
        if i > bigger:
            bigger = i
    return bigger




#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0

    
