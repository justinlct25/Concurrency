import asyncio

def number_generator(m, n):
    """ A number generator co-routine in range(m...n+1) """
    yield from range(m, n+1)

# @async_generator
async def prime_filter(m,n):
    """ Prime number co-routine"""
    primes = []
    for i in number_generator(m, n):
        if n == 2: yield n
        if n == 1 or n % 2 == 0: continue
        flag = True
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                flag = False
                break
        if flag:
            print('Prime=>',i)
            primes.append(i)
        # At this point the co-routine suspends execution so that another co-routine can be scheduled
    await asyncio.sleep(1,0)
    return tuple(primes)

# @async_generator
async def square_mapper(m,n):
    """ Square mapper co-routine """
    squares = []
    for i in number_generator(m, n):
        print('Square=>', i*i)
        squares.append(i*i)
        # At this point the co-routine suspends execution so that another co-routine can be scheduled
    await asyncio.sleep(1,0)
    return squares

def print_result(future):
    print('Result=>', future.result())


loop = asyncio.get_event_loop()
future = asyncio.gather(prime_filter(10, 50), square_mapper(10, 50))
future.add_done_callback(print_result)
loop.run_until_complete(future)

loop.close()