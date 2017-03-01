# Given a list of strings, define a procedure to return the count of strings starting with a upper case letter "U"
# 给定某一字符串列表，写一个函数，返回以大写字母U开头的字符串的个数
def measure_udacity(list_of_strs):
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
