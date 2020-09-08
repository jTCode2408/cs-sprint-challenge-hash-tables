''' ticket for your first flight has a destination with a `source` of
`NONE`, and the ticket for your final flight has a `source` with a
`destination` of `NONE`. '''
##########
''' Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]'''
###########
''' * We can hash each ticket such that the starting location is the key and
  the destination is the value. Then, when constructing the entire
  route, the `i`th location in the route can be found by checking the
  hash table for the `i-1`th location.'''
#  Hint:  You may not need all of these.  Remove the unused functions.
#use a lookup table
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    return route
