# A procedure named "bigger". Find out the bigger of out two radom numbers.
# 名为bigger的函数。在两个随机数字当中找出较大的那个数字。
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

# A procedure named "biggest". Find out the biggest of out three random numbers. I like this one very much.
# 名为biggest的函数。在三个随机数字当中找出最大的那个数字。我非常喜欢这一个。
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

# A procedure named "median". Find out the median one of out three random numbers. 
# 名为median的函数。在三个随机数字当中找出中间的那个数字。
def median(a,b,c):
    if bigger(a,b) <= c:
        return bigger(a,b)
    if bigger(a,c) <= b:
        return bigger(a,c)
    if bigger(b,c) <= a:
        return bigger(b,c)
    
