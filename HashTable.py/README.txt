##### ////// HashTable.py  \\\\\ #####
""" The HashTable class is an implementation of the hash table ADT. A test block is included below.
    Implemented using inbuilt Python list.
    Collisions are dealt with using linear probing for simplicity of code, the next non-empty index is used.
    Resizing list is done using prime numbers for effective hashing of keys which uses modular division.

    TO DO:
        *Will implement a function to update a value.
        *Will use pointers for beginning & end of list to fill up entire list before resizing (use space efficiently)
        *Will also use chaining in separate revision


    Function descriptions:
        printTable() - prints the entire hash table list
        getLength() - returns the number of key, value pairs within the list
        _hash(key) - receives any key as input and returns a hashed integer value <= length of the list
        __newKey(key) - same as _hash() function but increments input by one (used when collision occurs)
        __getitem__(index) - receives list index as input and returns the key, value pair or 'empty' if invalid
                            - assumption input is >= 0 and <= __maxLength
        __deleteEntry__(index) - receives list index as input and overwrites the value with 'empty'
                            - assumption input is >= 0 and <= __maxLength
        __setitem__(key, value) - receives a key & value as input, calls __hash(key) to get index and assigns tuple
                                of key value pair. Checks if load factor exceeded & calls __resize() if needed
        _getKeyHash(key) - receives key as input, calls _hash(key) to retrieve list index, Checks if key exists and
                                returns list index
        __resize() - Called when load factor exceeded, calls __getPrime(size) to retrieve new list size, reassigns
                    entries from old list to newly resized list
        __getPrime(size) - Receives list length as input, finds next prime number > size by calling __checkPrime(size),
                            returns new list size
        __checkPrime(num) - Receives integer as input, returns True if num is a prime number

"""