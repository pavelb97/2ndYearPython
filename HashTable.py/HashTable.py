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

import math

class HashTable():
    def __init__(self):
        self.__maxLength = 11
        self.__loadFactor = 0.75
        self.__length = 0
        self.__hashTable = ['empty' for i in range(0, self.__maxLength)]

    def printTable(self):
        print(self.__hashTable)

    def getLength(self):
        return self.__length

    def _hash(self, key):
        return hash(key) % self.__maxLength

    def __newKey(self, key):
        return hash(key+1) % self.__maxLength

    def __getitem__(self, index):
        return self.__hashTable[index]

    def __deleteEntry__(self, index):
        self.__hashTable[index] = "empty"

    def __setitem__(self, key, value):
        hashed_key = self._hash(key)
        self.__length += 1

        if self.__hashTable[hashed_key] != 'empty':
            while self.__hashTable[hashed_key] != 'empty':
                if self.__hashTable[hashed_key][0] == key:
                    self.__length -= 1
                    break
                hashed_key = self.__newKey(hashed_key)

        self.__hashTable[hashed_key] = (key, value)

        if self.__length / float(self.__maxLength) >= self.__loadFactor:
            self.__resize()

    def _getKeyHash(self, key):
        hashed_key = self._hash(key)
        if self.__hashTable[hashed_key] == "empty":
            return "Invalid key"

        if self.__hashTable[hashed_key][0] != key:
            original = hashed_key
            while self.__hashTable[hashed_key][0] != key:
                hashed_key = self._hash(hashed_key+1)
                if self.__hashTable[hashed_key] == "empty":
                    return "Invalid key"
                if hashed_key == original:
                    return "Invalid key"
        return hashed_key

    def __resize(self):
        self.__maxLength = self.__getPrime(self.__maxLength * 2)
        self.__length = 0
        old__hashTable = self.__hashTable
        self.__hashTable = ['empty'] * self.__maxLength
        for item in old__hashTable:
            if item != "empty":
                self[item[0]] = item[1]

    def __getPrime(self, size):
        while True:
            size += 1
            if self.__checkPrime(size) is True:
                break
        return size

    def __checkPrime(self, num):
        if num <= 1:
            return False
        elif num <= 3:
            return True

        if (num % 2 == 0) or (num % 3 == 0):
            return False
        for i in range(5, int(math.sqrt(num) + 1), 6):
            if (num % i == 0) or (num % (i+2) == 0):
                return False
        return True


if __name__ == '__main__':
    import random
    import string

    table = HashTable()

    def populateTable():
        entries = 10
        for i in range(0, entries):
            table[random.randint(0, 10000)] = ''.join(random.choice(string.ascii_letters) for i in range(0, 10))

    populateTable()
    table.printTable()

    table['abc'] = "test 0"
    getItemTestKey = table._getKeyHash('abc')
    getItemTest = table.__getitem__(getItemTestKey)
    print(getItemTest)

    table.__deleteEntry__(getItemTestKey)
    delItemTest = table.__getitem__(getItemTestKey)
    print(delItemTest)
