#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer and prints a visual representation (image) of an abacus setup for a given positive integer value.
# 任务：
# 定义一个函数print_abacus(整数)，向它传入一个正整数，打印出与该给定值相对应算盘的图形。

# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3
# 评分
# 1 星: solved the problem!
# 2 星: 6 < 代码行数 <= 9
# 3 星: 3 < 代码行数 <= 6
# 4 星: 0 < 代码行数 <= 3
def print_abacus(value):
    #row_list = ["|", "0", "0", "0", "0", "0", "*", "*", "*", "*", "*", " ", " ", " ", "|"]
    row_list_const = ["|", "0", "0", "0", "0", "0", "*", "*", "*", "*", "*", "|"]
    value_next = value
    for i in range(9, -1, -1):
        index_0 = value_next / (10 ** i)
        index_1 = 0 - (index_0 + 1)
        row_list_let = row_list_const[:]
        row_list_let.insert(index_1, (" " * 3))
        row_str = "".join(row_list_let)
        # value_next = value_next % (10 ** i)
        value_next %= (10 ** i)
        print row_str
