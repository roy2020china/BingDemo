# We have a number of One Pence stamps, Two Pence stamps, and Five Pence stamps. 
# Question: Given a value which is a postive whole number, how many Once Pence, Two Pence and Five Pence stamps do we need to make up that value? NO built-in functions, * or / operation. + and - operations only.
# 我们有数量不等的面值1分，2分和5分的邮票。
# 问题：给一个正整数数值，我们需要多少张1分，2分和5分的邮票？不使用内置函数，也不使用乘法或除法运算。仅使用加法和减法运算。
def number_of_a_pence (total_value, value_of_pence):
    number_of_pence = 0
    while total_value >= value_of_pence:
        total_value = total_value - value_of_pence
        number_of_pence = number_of_pence + 1
    return {'number_of_pence': number_of_pence, 'total_value':total_value}
def stamps(total_value):
    _5p = number_of_a_pence(total_value, 5)
    number_of_5p = _5p['number_of_pence']
    _2p = number_of_a_pence(_5p['total_value'], 2)
    number_of_2p = _2p['number_of_pence']
    _1p = number_of_a_pence(_2p['total_value'], 1)
    number_of_1p = _1p['number_of_pence']
    print number_of_5p, number_of_2p, number_of_1p
    return (number_of_5p, number_of_2p, number_of_1p)
