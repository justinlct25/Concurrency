import sys
from timeit import default_timer as timer

start_time = timer()

all_lists = []

for i in range(int(sys.argv[1])):
    num_list = map(int, open('numbers/numbers_%d.txt' % i).readlines())
    all_lists += num_list
    print('Length of list', len(all_lists))
    # print('Sorting')
    print('Sorting numbers_%d.txt...' % i)
    all_lists.sort()
    open('sorted_nums.txt', 'w').writelines('\n'.join(map(str, all_lists)) + '\n')
    # print('Sorted')
    print('Sorted numbers_%d.txt' % i)

# print(all_lists)
print('Sorting time using Counter: ', round(timer() - start_time, 3), 's')