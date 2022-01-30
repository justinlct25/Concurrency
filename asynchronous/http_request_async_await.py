import asyncio
import aiohttp
import async_timeout

@asyncio.coroutine
def fetch_page(session, url, timeout=60):
    """ Asynchronous URL fetcher """
    with async_timeout.timeout(timeout):
        response = session.get(url)
        return response

loop = asyncio.get_event_loop()
urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')

session = aiohttp.ClientSession(loop=loop)
tasks = map(lambda x: fetch_page(session, x), urls)
# Wait for tasks
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=120))

loop.close()

for future in done:
    response = future.result()
    print(response)
    response.close()
    session.close()

loop.close()

async def parse_response(futures):
    """ Parse responses of fetch """
    for future in futures:
        response = future.result()
        data = await response.text()
        print('Response for URL', response.url, '=>', response.status, len(data))
        response.close()

session = aiohttp.ClientSession(loop=loop)
# Wait for futures
tasks = map(lambda x: fetch_page(session, x), urls)
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=300))

# One more processing step to parse responses of futures loop.run_until_complete(parse_response(done))

session.close()
loop.close()