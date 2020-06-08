def has_negatives(a):
    """
    find positive elemnts that have negative elements in arra
    -limit 5,000,000
    """
    #version of lookup table?
    #dict to keep track of nums(a)
    #list of positive nums that have neg elemnts(to return)
    #traverse dict: to check numbers
    #if num = -num in the dict: add to list
    #keys =index
    #values =value

    dict ={}
    result = []

#traverse nums & add to dict
#start at 1st num index
    for num in a:
        dict[num] =1
    #check if - in dict
    #if is: add to list
    #need to get val of nums
        if num != 0 and -num in dict:
            result.append(abs(num))
            #abs allow me to not get -nums in return

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
