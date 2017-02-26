# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).
def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    length = len(product)
    #print length
    for each_character in product:
        #print each_character
        found = debris.find(each_character)
        #print found
        length = length - 1
        if found == -1:
            #if length > 0:
                result = "Give me something that's not useless next time."
                print result
                break
        if length == 0 and found > -1:
        #else:
                result = product
                print result
    return result
