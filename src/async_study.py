import asyncio
import time

async def hello_world():
    time.sleep(2)
    print("Hello World!")

    return 0

async def httpConnect():
    print("connecting...")
    time.sleep(6)
    print("connected")
    
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(hello_world())
# finally:
#     loop.close()



async def main():
    print("esperando as rotina principais...")
    await asyncio.gather(*[hello_world(), httpConnect()])
     
asyncio.run(main())