import sys
import collections
from timeit import default_timer as timer

MAXINT = 100000

def sort():
    """ Sort files on disk by using a counter """
    counter = collections.defaultdict(int)
    for i in range(int(sys.argv[1])): 
        filename = 'numbers/numbers_%d.txt' % i
        for n in open(filename):
            counter[n] += 1
    with open('sorted_nums.txt', 'w') as fp:
        for j in range(1, MAXINT+1): # loop from number 1 to 100000
            # count of the appearance of a number
            count = counter.get(str(j) + '\n', 0) # 0 is the default return value when the number(key) is not found
            if count>0:
                fp.write((str(j)+'\n') * count) # write the number(key) (count) times
    print('Sorted')

    
if __name__ == '__main__':
    start_time = timer()
    sort()
    print('Sorting time using Counter: ', round(timer() - start_time, 3), 's')

# python3 disk_files_sorting.py (sys.argv[1])
# eg. python3 disk_files_sorting.py 6, 6 is the number of the number files to be sorted / looped