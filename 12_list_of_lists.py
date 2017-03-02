# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).
# 定义一个名为total_enrollment的函数，传入一个列表，每个列表包含三项：大学名称，录取总人数，每年的学费。 
# 该函数应当返回两个数字，而不是一个字符串，即列表中各大学的录取总人数之和，以及学费总金额（学费总金额是每个大学录取人数乘以每个大学学费的乘积之和）


udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

# Solution 1 解决方案1
def total_enrollment(list_of_lists):
    total = [0, 0, 0]
    for each_list in list_of_lists:
        total[1] += each_list[1]
        total[2] += each_list[1] * each_list[2]
    return total[1], total[2]

# Solution 2 解决方案2  
  def total_enrollment(p):
    total_students = 0
    total_tuition = 0
    for name, students, price in p:  
        total_students += students   
        total_tuition += price
    return total_tuition, total_students

    # for i in p:
    #     students = i[1]
    #     price = i[2]
    #     total_students += total_students + students
    #     total_tuition += total_tuition + price
