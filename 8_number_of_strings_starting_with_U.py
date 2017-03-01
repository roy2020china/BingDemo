# Given a list of strings, define a procedure to return the count of strings starting with a upper case letter "U"
# 给定某一字符串列表，写一个函数，返回以大写字母U开头的字符串的个数

# version 1 版本1
def measure_u(list_of_strs):
    search_results = []
    for each in list_of_strs:
        search_for = "U"
        if start_U_or_not(search_for, each):
            search_results.append(each)
    return len(search_results)


def start_U_or_not(search_for, string):
    if string[0] == search_for:
        return True
    else:
        return False

    
# version 2 版本2
def measure_U(list_of_strs):
    count = 0
    for each in list_of_strs:
        if each[0] == "U":
            count += 1
    return count
