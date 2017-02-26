# 1st string inputs is called "debris", while 2nd string "product". Returns the 2nd input string as the output if all of its characters can be found in the 1st input string and "Give me something that's not useless next time." if it's impossible. 
# Letters that are present in the 1st input string may be used as many times as necessary to create the 2nd string.
# 第1个传数是名为debris的字符串，而第2个传参是名为product的字符串。如果第2个传参中的所有字母都可以在第1个传参中找到，那么返回第2个传参；否则，就返回Give me something that's not useless next time。
# 第1个传参中的字母可以使用任意多次。
def fix_machine_1(debris, product):
    ### WRITE YOUR CODE HERE ###
    length = len(product)
    #print length
    for each_character in product:
        #print each_character
        start_index = debris.find(each_character)
        #print found
        length = length - 1
        if start_index == -1:
            #if length > 0:
                result = "Give me something that's not useless next time."
                print result
                break
        if length == 0 and start_index > -1:
        #else:
                result = product
                print result
    return result

# Letters that are present in the 1st input string may be used ONLY ONCE to create the 2nd string.
# 第1个传参中的字母只可以使用一次。
def fix_machine_2(debris, product):
    ### WRITE YOUR CODE HERE ###
    debris_updated = debris
    length = len(product)
    #print length
    for each_character in product:
        #print each_character
        start_index = debris_updated.find(each_character)
        debris_updated = debris_updated[ : start_index] + debris_updated[ start_index + 1 : ]
        #print found
        length = length - 1
        if start_index == -1:
            #if length > 0:
                result = "Give me something that's not useless next time."
                print result
                break
        if length == 0 and start_index > -1:
        #else:
                result = product
                print result
    return result
    
