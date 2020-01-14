##### ////// anagrams.py - Lab from CS2516 \\\\\ #####
"""
    Comparing various complexities of file processing inclsuing inbuilt .append function, appending at the start and,
    appending a given index.
    Also compares linear and binary searches.

"""
import time
from time import perf_counter

def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations.txt', 'r')
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations


def performance_check(list1):
    """ Evaluate the performance of the functions.

    Note that the ...replace() function will take a long time to run
    on long input lists, and so that line should be commented out
    for lists of length > 100K.

    Args:
        list1: first list for processing

    """
    
    print('List length: %d' % len(list1))

    # run each function on the two lists, checking clock times in between

    # first the append method
    count_start_time = perf_counter()
    count_res = list_append(list1)
    count_end_time = perf_counter()
    print('Append method time      : %f' % (count_end_time - count_start_time))

    # then the append at start
    count_start_time = perf_counter()
    count_res = append_at_start(list1)
    count_end_time = perf_counter()
    print('Append at start time    : %f' % (count_end_time - count_start_time))

    # Finally inserting at list index
    count_start_time = perf_counter()
    count_res = indexing_position(list1)
    count_end_time = perf_counter()
    print('Inserting at list index : %f' % (count_end_time - count_start_time))

def list_append(all_stations):
    processedList = [item for item in all_stations]
    return processedList

def append_at_start(all_stations):
    processedList = []
    for item in all_stations:
        processedList.insert(0, item)
    return processedList

def indexing_position(all_stations):
    processedList = []
    listLength = len(all_stations)

    for index in range(0, listLength):
        processedList.insert(index, None)

    for index in range(0, listLength-1):
        processedList[index] = all_stations[index]

    return processedList

all_stations = read_garda_stations_tuples()
attempt1 = list_append(all_stations)                # List append


attempt2 = append_at_start(all_stations)
#print(attempt2)                                    # Append at start

attempt3 = indexing_position(all_stations)
#print(attempt3)                                    # indexing_position



performance_check(all_stations)

def linearSearch(item):
    count_start_time = perf_counter()
    for i in all_stations:
        for k in i:
            if item in k:
                count_end_time = perf_counter()
                print('Time taken: %f' % (count_end_time - count_start_time))
                return True
    count_end_time = perf_counter()
    print('Time taken: %f' % (count_end_time - count_start_time))
    return False


def binarySearch(item):
    count_start_time = perf_counter()
    i = 0
    start = 0
    end = len(all_stations)
    found = False

    while start <= len(all_stations) and not found:
        midpoint = (end + start) // 2
        if item == all_stations[midpoint][0]:
            found = True
            break
        elif item < all_stations[midpoint][0]:
            end = midpoint - 1
        elif item > all_stations[midpoint][0]:
            start = midpoint+1
    count_end_time = perf_counter()
    print('Time taken: %f' % (count_end_time - count_start_time))
    return found

print(linearSearch('Golden'))
print(binarySearch('Golden'))
