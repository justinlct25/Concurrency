import collections
from timeit import default_timer as timer

def number_generator(n):
    """ A co-routine that generates number in range 1...n """
    for i in range(1, n+1):
        yield i

def square_mapper(numbers):
    """ A co-routine task for converting numbers to squares """
    for n in numbers:
        yield n*n

def prime_filter(numbers):
    """ A co-routine which yields prime numbers """
    for n in numbers:
        if n == 2: yield n
        if n == 1 or n % 2 == 0: continue
        flag = True
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                flag = False
                break
        if flag:
            yield n

def scheduler(tasks, runs=10000):
    """ Basic task scheduler for co-routines """
    results = collections.defaultdict(list)
    for i in range(runs):
        print('Run',i+1,':')
        for t in tasks:
            print(' Switching to task', t.__name__)
            try:
                result = t.__next__()
                print(' result=>', result)
                results[t.__name__].append(result)
            except StopIteration:
                break
    return results




import sys

tasks = []
start = timer()

limit = int(sys.argv[1])

# Append square_mapper tasks to list of tasks
tasks.append(square_mapper(number_generator(limit)))
# Append prime_filter tasks to list of tasks
tasks.append(prime_filter(number_generator(limit)))

results = scheduler(tasks, runs=limit)
# print(results)
print('Process ended')
print('Time taken=>', round(timer() - start, 5), 's')
print('Last square=>', results['square_mapper'][-1])
print('Last prime=>', results['prime_filter'][-1])

# python3 multitasking_scheduler.py 9999