# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
# 定义一个名叫find_last的函数，传入两个参数均为字符串，一个是搜索字符串，另一个是目标字符串。
# 功能实现：目标字符串在搜索字符串中最后一次出现的位置；如果目标字符串从未出现过，则返回 -1。
#

def find_last(search_str, target_str):
    start_index = search_str.find(target_str)
    if start_index == -1: 
        return start_index   
    
    while start_index != -1: 
        last_index = start_index 
        start_index = search_str.find(target_str, start_index + 1)
    return last_index
