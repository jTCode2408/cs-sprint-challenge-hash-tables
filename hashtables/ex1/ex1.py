'''* If we store each weight's list index as its value, we can then check
  to see if the hash table contains an entry for `limit - weight`. If it
  does, then we've found the two items whose weights sum up to the
  `limit`!
  _Tuple with higher val first, lower val 2nd that = limit to return '''
  #what will keys be? -weight?
  #values? weight value
  #add weights to dict
  #traverse weights in dict
  #find 2nd key(weight) that is = to 1st weight +2nd weight =limit
  #limit - weight 1 =weight2? 
  #return both weights
def get_indices_of_item_weights(weights, length, limit):
    dict = {}
    #add weightd to dict 
    #'current' weight index at(key)
    for cur in range(0, length):
        dict[weights[cur]] =cur
#from cur index:
#check for weight2 that = limit-weight1
#
    for cur in range(0, length):
        if limit - weights[cur] in dict:
            w1  =cur
            w2 =dict[limit - weights[cur]]
            if w1 < w2:
                w1, w2 = w2, w1
            return (w1, w2)

    return None

