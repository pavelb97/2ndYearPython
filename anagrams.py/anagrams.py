##### ////// anagrams.py - Lab from CS2516 \\\\\ #####
""" Example functions for comparing methods of checking anagrams (as lists).

    Contains four main functions
        isAnagramReplace: for each element in the 1st list, find a match in the 2nd and replace it with a null character.
        isAnagramCount: for each element in the alphabet, count the number of times it appears in each list,
                        and make sure they are all the same
        isAnagramSort: sort the two lists, and then step through them in parallel, checking the elements match
        isAnagramDict: same as ...Count, but using a Python dict

    The alphabet is integers from 0 to 9999.
    
    Also contains some performance evaluation functions.

    To run, invoke perf_check_random(k), where k is the length of a pair of
    random lists to be checked for being anagrams.
"""

import time
from time import perf_counter

import random

def performance_check(list1, list2):
    """ Evaluate the performance of the anagram functions.

    The ...replace() function will take a long time to run on long input lists, and so that line should be commented out
    for lists of length > 100K.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    """
    
    print('List length: %d' % len(list1))

    # run each function on the two lists, checking clock times in between

    # first the count method
    count_start_time = perf_counter()
    count_res = is_anagram_count(list1, list2)
    count_end_time = perf_counter()
    print('Count time    : %f %s' % (count_end_time - count_start_time,
                                     count_res))

    # then the dict method
    count_start_time = perf_counter()
    count_res = is_anagram_dict(list1, list2)
    count_end_time = perf_counter()
    print('Dict time     : %f %s' % (count_end_time - count_start_time,
                                     count_res))


    # now the sort method
    # create copies, so that we don't change data for later methods
    if len(list1) < 3000000:
        copylist1 = list1.copy()
        copylist2 = list2.copy()
        sort_start_time = perf_counter()
        sort_res = is_anagram_sort(copylist1, copylist2)
        sort_end_time = perf_counter()
        print('Sort time     : %f %s' % (sort_end_time - sort_start_time,
                                         sort_res))


        # now do a quick check on the time required just for sorting
        # do this before the replace function, because it changes the lists
        copylist3 = list1.copy()
        copylist4 = list2.copy()
        waypoint_time = perf_counter()
        copylist3.sort()
        copylist4.sort()
        end_time = perf_counter()
        # now print the stats for the pure sort
        print('   pure sort time: %f' % (end_time - waypoint_time))

    else:
        print('Lists too long to run the sort method')

    # now the replace method
    if len(list1) < 30000:
        replace_start_time = perf_counter()
        replace_res = is_anagram_replace(list1, list2)
        replace_end_time = perf_counter()
        print('Replace time  : %f %s' % (replace_end_time - replace_start_time,
                                         replace_res))
    else:
        print('Lists too long to run the replace method')
        

    

def correctness_check(list1, list2):
    """ Test the correctness of anagram functions.

    Args:
        list1: first list for comparison
        list2: second list for comparison
    """

    print('List 1: %s' % list1)
    print('List 2: %s' % list2)

    # run each function on the two lists

    # first the count method
    print('count: %s' % is_anagram_count(list1, list2))

    # then the dict method
    print('dict: %s' % is_anagram_dict(list1, list2))

    # now the sort method
    # create copies, so that we don't change data for later methods
    copylist1 = list1.copy()
    copylist2 = list2.copy()
    print('sort: %s' % is_anagram_sort(copylist1, copylist2))

    # now the replace method
    print('replace: %s' % is_anagram_replace(list1, list2))


def perf_check_random(k):
    """ Compare performance on random lists of length k.

    Lists must be composed of elements in {0, ..., 999}

    Args:
        k: (int) length of lists

    """

    if k < 1:
        return False

    # generate a random list of length k, then copy it and shuffle the copy
    # then call performance_check on the lists
    rand_list = list()    
    for i in range(k):
        rand_list.append(random.randint(0,9999))
    second_list = rand_list.copy()
    #random.shuffle(second_list)
    performance_check(rand_list, second_list)
    
    
def is_anagram_replace(list1, list2):
    """ Check whether two lists are anagrams, by replacement.

    For each element in the first string, find a match in the second and
    replace it by a null value.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and all elements replaced
        false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False
                                           
    for pos1 in range(len(list1)):      # for each element in list1
        found = False                   # found a match for list1[pos1] yet?
        pos2 = 0
        while pos2 < len(list2) and not found:  # step list2 looking for match
            if list1[pos1] == list2[pos2]:      # if we find the match
                found = True
                list2[pos2] = None              # replace element in the list
            pos2 += 1

        if not found:                       # if we didn't find a match
            return False                    # prefix is not in list2

    return True
        

def is_anagram_sort(list1, list2):
    """ Check whether two lists are anagrams, by sorting and comparing.

    Sort the lists, then step through in parallel checking that the
    elements match

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
           true if lists of same length and all elements match
           false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False

    list1.sort()                   # sort each list
    list2.sort()

    for pos in range(len(list1)):         # step through the lists in parallel
        if list1[pos] != list2[pos]:      # if elements don't match
            return False                  # it can't be an anagram

    return True                          

def is_anagram_count(list1, list2):
    """Check whether two lists are anagrams, by counting elements.

       Lists must be composed of elements in {0, ..., 999}
       
       For each element in the alphabet, count +1 for each time it appears
       in the 1st list, and -1 for each time in the second.
       Iterate through the lists in parallel, rather than doing a separate
       sweep for each element

    Args:
        list1: first list for comparison
        list2: second list for comparison

       Returns:
           true if lists of same length and all elements have count 0
           false otherwise
    """

    if len(list1) != len(list2): # anagrams must be same length
        return False

    count_list = [0] * 10000    # the counters for each element in the alphabet

    for i in range(len(list1)):      # step through each position in turn
        elt1 = list1[i]              # element from list1
        count_list[elt1] += 1   # increment counter for elt1
        elt2 = list2[i]              # element from list2
        count_list[elt2] -= 1   # decrement counter for elt2

    for pos in count_list:
        if pos != 0:
            return False              # if any element is non-zero

    return True

def is_anagram_dict(list1, list2):
    """ Check whether two lists are anagrams, by counting elements using a dict.

    Lists must be composed of elements in {0, ..., 999}

    Create an empty dictionary, with keys in {0, ..., 999}, and values
    the number of appearances in list1 minus the number in list2. If an
    integer does not appear as a key in the dict, then it has not appeared
    in either list.
    For each position in the lists, for the elt in list1, add 1 to the
    value for the key corresponding to that elt, and create a new entry with
    value 1 if there is no such key; for the elt in list2, do the same, but
    use -1 in each case.
    for each key in the dict, if the value is not 0, return false.
    return true.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and all elements have count 0
        false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False

    count = {}

    for i in range(len(list1)):          # step through each position in turn
        count[list1[i]] = count.get(list1[i],0) + 1  # incr value or set to 1
        count[list2[i]] = count.get(list2[i],0) -1
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
        if list2[i] in count:
            count[list2[i]] -= 1
        else:
            count[list2[i]] = -1

    for key in count:
        if count[key] != 0:
            return False              # if any element is non-zero
    return True

perf_check_random(10)
print("#########")
perf_check_random(100)
print("#########")
perf_check_random(1000)
print("#########")

