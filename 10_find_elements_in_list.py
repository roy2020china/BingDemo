# Find the first occurrence of the target value in a given list, and return its index
# 在给定列表中寻找特定值首次出现的位置，并返回其指针。

# use for loop 
def find_element(a_list, target_value):
     i = 0
     for each in a_list:
         # print each
         if each == target_value:
             return i
         i += 1
     return -1
    
#use while loop    
def find_element(a_list, target_value): 
    i = 0
    while a_list[i] != target_value:
        i += 1
        if i >= len(a_list):
            return -1
    return i
