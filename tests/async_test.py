import asyncio

def async_test(f):
    def wrapper(*args , **kwargs):
        coroutine  = asyncio.coroutine(f)
        future =  coroutine(*args , **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper