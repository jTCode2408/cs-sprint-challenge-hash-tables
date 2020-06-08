"""
numbers that exist in all lists.
* There can be up to 10 lists in the list of lists.
* The lists can contain up to roughly 1,000,000 elements each.
"""
def intersection(arrays):
    #dict for vals
    #needd to loop over arrays, & each array in arrays
    #need to keep count of elms in arr of arrays
    # loop over each array in arrays
    #check if val is in dict
    #return: vals that are in arrays
    dict ={}
    result = []

    for arr in arrays:
        for i in arr:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] =1
    
    for (key, value) in dict.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
