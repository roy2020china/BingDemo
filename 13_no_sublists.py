# Write a procedure, input a list with sublist elements, and output a list with no sublists.
# 写一个函数，输入一个含有列表的列表，输出一个不含有列表的列表。
# input /输入：[1, [2, 0], [3, 0, [4, 7, 5]]]
# output /输出： x = [1, 2, 0, 3, 0, 4, 7, 5]


def get_final_list(a_list):
    final_list = []
    to_check = a_list
    #print to_check
    while to_check:
        if isinstance(to_check[0], list) or isinstance(to_check[0], tuple):
            new_list = to_check[0]
            del to_check[0]
            #print to_check
            to_check = new_list + to_check  # NOT to_check += new_list
            #print to_check
        else:
            final_list.append(to_check[0])
            del to_check[0]
    #print final_list
    return final_list


def is_sublist(i):
       if isinstance(i, list) or isinstance(i, tuple):
            return True
       else:
            return False


# x = [1, [2, 0], [3, 0, [4, 7, 5]]]
# print get_final_list(x)
# >>>[1, 2, 0, 3, 0, 4, 7, 5]
