Notes on topics in 'Interview Questions' section

1. Hashing functions
-transform string, (or other data) into numbers
-bytes make up string(can use .encode fn to get bytes)
-each letter has a # assigned to it (aasci)
-should return same val each time with same input
-must return numbers within a specific range


2. Collision resolution
-Instead of 1 element at slot, will hold a linkedlist at that slot with pointers for each val at index slot
-If collision happens, add item to LL instead of overwriting
-save key & value in LL to reference
-search for elemnts by key to get values
-can also use 'probing' (if slot is full, look ahead for open slot. runtime may increase, or may be no empty slots)

3. Performance of basic hash table operations
-O(1) average or O(n) because the hashing fn is constant
-able to search faster without sorting, and use large data sets
-The larger the load factor, the worse the performance(but resizing can help this)

4. Load factor
-How many elements in table divded by how many slots in table
-(can be more elements than slots if collisions exist)
-once number of collisions gets to high, build a new table to help reduce collisions/spead up time


5. Automatic resizing
-When load factor gets 'overloaded':
-Make a new hashtable with more slots-typically double the old[or half if making smaller]
(copy elements in the original hashtable)
-Each element in the old table will be re-hashed into slots in the bigger hashtable
-will allow load factor to decrease


6. Various use cases for hash tables
-for working with large data sets
-search for elements
-store and get elements
-finding elemnts by key
