import multiprocessing
import sys
import collections
from timeit import default_timer as timer


MAXINT = 100000

def sorter(filenames):
    """ Sorter process sorting files using a counter """
    counter = collections.defaultdict(int)
    for filename in filenames:
        for i in open(filename):
            counter[i] += 1
            return counter

def batch_files(pool_size, limit):
    """ Create batches of files to process by a multiprocessing Pool """
    batch_size = limit // pool_size
    filenames = []
    for i in range(pool_size):
        batch = []
        for j in range(i*batch_size, (i+1)*batch_size):
            filename = 'numbers/numbers_%d.txt' % j
            batch.append(filename)
    return filenames

def sort_files(pool_size, filenames):
    """ Sort files by batches using multiprocessing Pool """
    with multiprocessing.Pool(pool_size) as pool:
        counters = pool.map(sorter, filenames)
        with open('sorted_nums.txt', 'w') as fp:
            for i in range(1, MAXINT+1):
                count = sum([x.get(str(i)+'\n',0) for x in counters])
                if count>0:
                    fp.write((str(i)+'\n')*count)
    print('Sorted')

if __name__ == "__main__":
    limit = int(sys.argv[1])
    pool_size = 4
    filenames = batch_files(pool_size, limit)
    start_time = timer()
    sort_files(pool_size, filenames)
    print('Time used with multiprocessing', round(timer() - start_time, 2), 's')