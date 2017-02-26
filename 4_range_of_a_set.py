#range of a set
# Define a procedure, set_range, which returns the range of three input values.  The range of a set of values is the maximum value minus the minimum value.
# 一组数字的范围
# 定义一个名为set_range的函数，它可以返回三个输入的值的范围，即三个数值当中最大值与最小值之差。

def set_range(a,b,c):
    results = biggest_and_smallest(a,b,c)
    range_is = results["biggest"] - results["smallest"]
    print range_is
    return range_is
def big_and_small(a,b):
    if a > b :
        result = {"big":a, "small":b}
    else:
        result = {"big":b, "small":a}
    return result
def biggest_and_smallest(a,b,c):
    biggest = big_and_small(a, big_and_small(b,c)["big"])["big"]
    smallest = big_and_small(a, big_and_small(b,c)["small"])["small"]
    return {"biggest": biggest, "smallest": smallest}
